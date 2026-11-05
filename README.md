# UML Documentation

Skill para conduzir descoberta de requisitos e documentar software em Markdown e PlantUML. Pode ser usada antes de existir código, para definir escopo, MVP, etapas, critérios de aceitação e baselines, ou com uma implementação existente, para registrar o comportamento observado e compará-lo com os requisitos aprovados.

## O que gera

- Requisitos funcionais e não funcionais, regras e critérios de aceitação.
- Catálogo de casos de uso com descrições completas.
- Código PlantUML dos diagramas de casos de uso, classes e sequência.
- Matriz de rastreabilidade entre requisitos, casos, código, testes e lacunas.

Os arquivos são criados ou atualizados na pasta documental do projeto, normalmente `docs/`. Nomes, IDs e decisões já existentes são preservados. A análise diferencia comportamento observado, intenção confirmada, inferências e cenários realmente testados.

## Instalação e uso

Copie esta pasta para a pasta de skills do Codex, normalmente `~/.codex/skills/umldocumentation`, mantendo `SKILL.md` na raiz da skill.

Exemplo de solicitação:

```text
Use $umldocumentation para analisar este projeto e gerar requisitos,
casos de uso detalhados e diagramas PlantUML na pasta docs.
```

Também é possível indicar raízes de vários projetos. A skill mantém a documentação e a cobertura separadas por projeto.

Para iniciar sem código, peça: `Use $umldocumentation para entrevistar-me sobre o projeto, propor um MVP e registrar as decisões e os requisitos.`

## Inventário auxiliar

O inventariador requer Python 3.10+. Com `rg` disponível, respeita suas regras de exclusão. O fallback sem `rg` informa que não interpreta `.gitignore`.

```text
python scripts/inventory.py /caminho/do/projeto --output /caminho/do/projeto/docs/INVENTARIO_CODIGO.json
```

Para atualizar explicitamente um inventário existente, acrescente `--force`. Sem essa opção, um arquivo de destino existente é preservado.

O script lista caminhos e metadados; não interpreta o comportamento do programa nem gera sozinho os documentos. A leitura semântica e a produção documental são feitas pela IA seguindo a skill. As exclusões de arquivos sensíveis são heurísticas e os candidatos devem ser revisados antes da leitura.

## Estrutura

```text
SKILL.md                       Instruções de análise e geração
agents/openai.yaml             Metadados para seleção no Codex
scripts/inventory.py           Inventário de candidatos à análise
references/documentation.md    Conteúdo documental e rastreabilidade
references/plantuml.md         Modelagem e validação dos diagramas
references/requirements-discovery/  Entrevistas, escopo, MVP e versionamento
```

## Limites

- A documentação gerada precisa preservar a diferença entre implementação e requisito aprovado.
- Inventariar arquivos não significa ter analisado todo o código.
- Dependências, arquivos gerados, segredos e links externos são excluídos por padrão; as limitações de cobertura devem ser registradas.
- Diagramas só são declarados compilados ou renderizados quando essa verificação realmente ocorrer.
- Não há monitoramento contínuo ou publicação automática. A skill atua no escopo da tarefa indicada.
- Não executa uma auditoria completa de segurança nem certifica conformidade do software.
