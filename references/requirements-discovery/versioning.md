# Versionamento documental

Existem três identificadores independentes: versão desta skill, versão da especificação do projeto e versão do software descrito. Nunca incremente um deles como consequência automática da mudança de outro.

## Histórico e baseline

Use Git para histórico detalhado quando disponível. Preserve convenções de branches e commits do repositório. Rascunhos podem evoluir em commits sem nova release formal. Uma baseline identifica um conjunto de requisitos aprovado para uma etapa, com data, escopo, responsável pela confirmação e referência imutável quando disponível (tag ou commit).

Um commit ou uma tag não comprova aprovação de negócio. Não invente confirmação, hash ou data. Se ainda não houver Git, mantenha versão, estado e registro de alterações no próprio conjunto documental, sem afirmar que existe histórico Git.

## Convenção proposta para a especificação

Respeite a convenção existente. Na ausência dela, proponha `MAJOR.MINOR.PATCH` com este significado explícito:

- MAJOR: alteração incompatível com acordos aprovados, como retirada de capacidade ou mudança em regra que invalida critérios anteriores.
- MINOR: inclusão compatível de requisitos ou detalhamento que amplia o escopo sem invalidar os acordos anteriores.
- PATCH: correção editorial, de link ou esclarecimento que não muda o comportamento acordado.

Se um esclarecimento mudar o comportamento esperado, não o classifique como editorial. Antes da primeira aprovação, use estado rascunho e, se necessário, versões `0.x.y`. Estabeleça `1.0.0` da especificação apenas quando houver uma primeira baseline aprovada; a publicação desta skill em `1.0.0` não aprova projetos futuros.

Registre a versão documental, estado, data e relação com versões previstas ou entregues do produto. Use “a definir” quando não conhecidas. Não prometa sincronização entre as duas numerações.

## Procedimento de mudança

1. Identifique a solicitação, fonte, motivo e requisitos afetados.
2. Compare com a baseline atual e avalie impacto em escopo, esforço, dados, acesso, integrações, critérios e etapas.
3. Registre proposta e alternativas; obtenha decisões necessárias sem bloquear trabalho independente.
4. Atualize os documentos relacionados de forma coerente. Preserve IDs e registre substituições ou descontinuações.
5. Registre o que mudou, por quê, estado da aprovação e eventual versão documental correspondente.

Evite manter cópias completas em pastas `v1`, `v2`, `final`: prefira histórico Git e baselines identificáveis. Não apague o histórico nem reescreva tags publicadas.

## Publicação

Prepare commit, tag ou release apenas dentro da autorização recebida. Antes de publicar, confira diff, arquivos incluídos, pendências, links e ausência de segredos ou dados pessoais desnecessários. Informe exatamente o que foi publicado e o que continua rascunho. Se a publicação falhar, preserve os arquivos e relate o estado real.
