# Conteúdo documental e rastreabilidade

## Cabeçalho comum

Identifique projeto, versão do software quando conhecida, versão documental separada, data e fonte analisada (commit e estado local, ou ausência de Git). Use caminhos relativos para referências internas e não inclua dados pessoais ou segredos. A primeira especificação extraída do código é um rascunho do comportamento observado, não uma baseline comercial aprovada.

## REQUISITOS.md

Defina objetivo, fronteira, atores, dependências, configuração necessária e exclusões. Para cada requisito, preserve ou atribua um ID estável, como RF-001, RNF-001 ou RN-001. Registre:

- Obrigação observável e justificativa/origem.
- Estado da decisão (confirmado, inferido/proposto, rejeitado ou descontinuado) separado do estado de entrega (observado, implementado segundo fonte, testado em execução ou pendente).
- Critério de aceitação verificável, incluindo falhas/limites quando relevante.
- Prioridade/etapa quando conhecidas; caso contrário, a definir.
- Evidências de implementação e relação com casos/testes.

Não converta cada método em requisito. Requisitos funcionais descrevem capacidades; regras descrevem condições de negócio; não funcionais descrevem propriedades verificáveis e restrições. Quando o projeto não define latência, disponibilidade, capacidade ou conformidade, registre a lacuna em vez de inventar metas. Uma proteção encontrada no código pode ser descrita como controle observado sem afirmar que garante segurança completa.

## CASOS_DE_USO.md

Inclua catálogo e descrições no mesmo arquivo, com IDs UC-001 etc. Para cada caso, informe objetivo, atores principal/de apoio, gatilho, pré-condições, fluxo principal numerado, alternativas ligadas ao passo correspondente, erros, pós-condições de sucesso/falha, requisitos e evidências. Se o sistema for biblioteca, serviço ou CLI, identifique consumidores e objetivos apropriados; não force telas e visitantes.

Use objetivos do ator como casos de uso; rotinas automáticas podem ser subfluxos claramente identificados. Diferencie sessão válida, permissão para a ação e acesso ao recurso. Considere operação repetida, configuração desativada, indisponibilidade da dependência e resultado parcial quando o código tratar essas condições. Não invente alternativas de erro específicas quando a implementação só retorna uma falha genérica.

Cadastros, OAuth, checkout, recuperação de senha e vinculação podem ser delegados; identifique o fornecedor, a interface e o limite do que foi lido/testado. Código de integração não comprova o comportamento completo da dependência.

## RASTREABILIDADE.md

Mantenha duas matrizes compactas:

1. **Cobertura:** módulo/caminho, pontos de entrada relevantes, estado de análise (inventariado, lido, rastreado, execução realizada, não analisado), exclusões e motivo.
2. **Relações:** requisito → caso/subfluxo → diagrama/bloco → arquivo/símbolo → teste existente → execução/evidência ou pendência.

Não repita as descrições completas nem copie o código. Registre divergências código/especificação, comportamentos não representados, perguntas abertas e limitações. Ausência de teste é uma informação útil. Não declare cobertura integral por ter listado todos os arquivos.

## Atualizações

Leia os documentos existentes antes de editar. Preserve IDs; registre descontinuação sem reutilizá-los. Atualize descrições e diagramas afetados, conservando decisões válidas. Não incremente a versão do software por alteração documental. Evite cópias `final`, `v2` ou snapshots integrais quando Git e um breve histórico documental bastarem.

## Verificação documental

Verifique se todos os casos apontam a requisitos válidos, todos os atores existem no catálogo, os símbolos diagramados estão no código ou marcados como externos/propostos, os links locais existem e o estado de validação é coerente entre os arquivos. A revisão não exige executar o aplicativo ou alterar a implementação.
