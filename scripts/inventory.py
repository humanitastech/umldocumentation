#!/usr/bin/env python3
"""List code/documentation candidates and coverage limits; never infer requirements."""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

SKIP_DIRS = {
    '.git', '.svn', '.hg', '.idea', '.vs', '.venv', 'venv', 'env',
    'node_modules', 'vendor', '__pycache__', '.pytest_cache', '.mypy_cache',
    '.next', '.nuxt', 'coverage', 'dist', 'build', 'target', 'bin', 'obj',
    '.cache', 'dependencies', '.aws', '.ssh', '.gnupg', '.azure',
}
SECRET_NAMES = {'.env', '.npmrc', '.pypirc', '.netrc', '.git-credentials',
                'wp-config.php', 'credentials.json', 'service-account.json',
                'id_rsa', 'id_ed25519', 'credentials', 'secrets.json', 'secrets.yaml', 'secrets.yml'}
SECRET_SUFFIXES = {'.pem', '.key', '.p12', '.pfx', '.kdbx', '.jks', '.keystore'}
SOURCE_SUFFIXES = {
    '.php', '.py', '.js', '.jsx', '.ts', '.tsx', '.mjs', '.cjs', '.vue', '.svelte',
    '.html', '.htm', '.css', '.scss', '.sass', '.less', '.java', '.kt', '.kts',
    '.cs', '.fs', '.vb', '.go', '.rs', '.c', '.h', '.cpp', '.hpp', '.cc', '.swift',
    '.m', '.mm', '.rb', '.r', '.jl', '.dart', '.ex', '.exs', '.erl', '.hrl', '.scala',
    '.clj', '.cljs', '.sql', '.graphql', '.gql', '.proto', '.sh', '.ps1', '.bat',
    '.cmd', '.lua', '.pl', '.pm', '.prisma', '.ipynb', '.ipynb-disabled',
}
DOC_SUFFIXES = {'.md', '.mdx', '.rst', '.adoc', '.puml', '.plantuml', '.mdl'}
CONFIG_SUFFIXES = {'.json', '.yaml', '.yml', '.toml', '.xml', '.ini', '.cfg', '.lock'}
CONFIG_NAMES = {'dockerfile', 'makefile', 'gemfile', 'rakefile', 'procfile',
                'license', 'license.txt', 'readme', '.gitignore', '.gitattributes'}


def is_link(path: Path) -> bool:
    return path.is_symlink() or getattr(path, 'is_junction', lambda: False)()


def git_info(root: Path) -> dict:
    if not shutil.which('git'):
        return {'available': False}
    def run(*args):
        result = subprocess.run(['git', '-C', str(root), *args], capture_output=True,
                                text=True, timeout=15, check=False)
        return result.stdout.strip() if result.returncode == 0 else None
    commit = run('rev-parse', 'HEAD')
    branch = run('symbolic-ref', '--short', '-q', 'HEAD')
    status = run('status', '--porcelain', '--untracked-files=normal')
    return {'available': status is not None, 'commit': commit, 'branch': branch,
            'has_local_changes': bool(status) if status is not None else None}


def blocked(relative: Path) -> str | None:
    parts = [p.lower() for p in relative.parts]
    if any(p in SKIP_DIRS for p in parts[:-1]):
        return 'dependency_or_generated_directory'
    name = parts[-1]
    if (name in SECRET_NAMES or name.startswith('.env.') or name.startswith('credentials.')
            or name.startswith('service-account') or Path(name).suffix in SECRET_SUFFIXES):
        return 'secret_candidate'
    # Examples may still be inventoried, but are never opened by this helper.
    if name.endswith(('.min.js', '.min.css', '.map')):
        return 'generated_asset'
    if name.endswith(('.dump', '.sqlite', '.sqlite3', '.db', '.bak', '.sql.gz')) or 'dump' in name and name.endswith('.sql'):
        return 'data_dump_candidate'
    return None


def classify(relative: Path) -> str | None:
    suffix = relative.suffix.lower()
    name = relative.name.lower()
    if suffix in DOC_SUFFIXES:
        return 'documentation'
    if suffix in SOURCE_SUFFIXES:
        parts = [p.lower() for p in relative.parts]
        return 'test' if any(p in {'test', 'tests', '__tests__', 'spec', 'specs'} for p in parts) or '.test.' in name or '.spec.' in name else 'source'
    if suffix in CONFIG_SUFFIXES or name in CONFIG_NAMES:
        return 'configuration_or_manifest'
    return None


def fallback_files(root: Path):
    for current, dirs, files in os.walk(root, followlinks=False):
        dirs[:] = sorted(d for d in dirs if d.lower() not in SKIP_DIRS
                         and not is_link(Path(current) / d))
        for name in sorted(files):
            yield (Path(current) / name).relative_to(root)


def collect(root: Path, output: Path | None) -> dict:
    counts = Counter()
    tool = shutil.which('rg')
    warnings = [
        'Inventory contains paths and metadata only; semantic code reading is still required.',
        'Secret filtering is heuristic; review candidates before opening content.',
        'Dependency/generated directories and symlink/junction targets are excluded.',
        'Ignored, unsupported and nontext files may contain behavior; declare coverage limits.',
        'Exclusion counts cover enumerated candidates only, not directories pruned by discovery.',
    ]
    if tool:
        result = subprocess.run([tool, '--files', '--hidden', '-0', '-g', '!.git/**'],
                                cwd=root, capture_output=True, check=False, timeout=120)
        if result.returncode not in (0, 1):
            raise RuntimeError('rg inventory failed; no complete inventory was produced.')
        candidates = [Path(os.fsdecode(p)) for p in result.stdout.split(b'\0') if p]
        mode = 'rg (respects rg ignore rules)'
    else:
        candidates = fallback_files(root)
        mode = 'os.walk fallback (does not interpret .gitignore)'
        warnings.append('rg is unavailable; fallback may list ignored first-party files.')
    entries = []
    for relative in candidates:
        path = root / relative
        try:
            resolved = path.resolve()
            if not resolved.is_relative_to(root):
                counts['outside_root'] += 1
                continue
            # Protect all path components, not only a linked final filename.
            current = root
            linked = False
            for component in relative.parts:
                current = current / component
                if is_link(current):
                    linked = True
                    break
            if linked:
                counts['link_or_junction'] += 1
                continue
            if output and resolved == output:
                counts['inventory_output'] += 1
                continue
            reason = blocked(relative)
            if reason:
                counts[reason] += 1
                continue
            role = classify(relative)
            if role is None:
                counts['unsupported_or_binary'] += 1
                continue
            size = path.stat().st_size
            if size > 2_000_000:
                counts['oversized_candidate'] += 1
                continue
            entries.append({'path': relative.as_posix(), 'role': role,
                            'extension': relative.suffix.lower(), 'bytes': size,
                            'analysis_state': 'inventoried_only'})
        except (OSError, ValueError):
            counts['unreadable_metadata'] += 1
    entries.sort(key=lambda item: item['path'])
    return {'schema_version': 1, 'project': root.name,
            'generated_at_utc': datetime.now(timezone.utc).isoformat(),
            'git': git_info(root), 'discovery': mode, 'warnings': warnings,
            'exclusion_counts': dict(sorted(counts.items())),
            'role_counts': dict(sorted(Counter(e['role'] for e in entries).items())),
            'files': entries}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', type=Path)
    parser.add_argument('--output', type=Path, help='JSON destination; omit for stdout')
    parser.add_argument('--force', action='store_true', help='Replace an existing inventory explicitly')
    args = parser.parse_args()
    root = args.root.resolve()
    if not root.is_dir():
        parser.error('Project root must be an existing directory.')
    output = args.output.absolute() if args.output else None
    if output and (is_link(output) or output.exists() and not args.force):
        parser.error('Output exists or is a link; choose another destination or use --force for an inventory.')
    if output:
        output = output.resolve()
        if output == root or output.suffix.lower() != '.json':
            parser.error('Output must be a .json file.')
    try:
        report = collect(root, output)
        text = json.dumps(report, ensure_ascii=False, indent=2) + '\n'
        if output:
            output.parent.mkdir(parents=True, exist_ok=True)
            # Exclusive creation prevents accidentally replacing a newly created file.
            with output.open('w' if args.force else 'x', encoding='utf-8') as stream:
                stream.write(text)
            print(f"Inventoried {len(report['files'])} candidates; semantic analysis not performed.")
        else:
            print(text, end='')
        return 0
    except (OSError, RuntimeError, subprocess.TimeoutExpired) as error:
        print(f'Inventory failed: {error}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
