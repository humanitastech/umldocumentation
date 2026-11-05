# Estrutura e qualidade da documentação

Adapte os nomes à estrutura existente. Para um projeto novo, um ponto de partida enxuto é `docs/requirements/overview.md`, `requirements.md`, `roadmap.md` e `decisions.md`. Separe diagramas, glossário ou matriz de acesso apenas quando o volume justificar. Não crie arquivos vazios.

## Visão e descoberta

Registre problema, público, envolvidos e responsáveis por decisões, objetivos e medidas de sucesso, escopo incluído/excluído, restrições, integrações, premissas e questões abertas. Identifique a fonte e a data de decisões relevantes. Ausência de resposta deve continuar visível.

## Requisitos

Use IDs por categoria, como RF-001 (funcional), RNF-001 (qualidade), RN-001 (regra de negócio), UC-001 (caso de uso) e DEC-001 (decisão). Adapte os prefixos existentes; nunca renumere para fechar lacunas nem reutilize IDs descontinuados.

Para cada requisito, registre:

- ID e título; enunciado inequívoco e observável.
- Necessidade e origem: quem solicitou ou qual evidência fundamenta o item.
- Estado da decisão: proposto, aprovado, rejeitado ou descontinuado.
- Estado de entrega separado: não iniciado, em andamento, implementado ou validado, somente com evidência disponível.
- Prioridade, etapa e dependências; versão prevista/entregue se conhecidas.
- Critérios de aceitação e regras relacionadas.
- Dúvidas, exceções e fontes relevantes.

Exemplo ilustrativo, que não constitui requisito aprovado de nenhum projeto:

> RF-001 — Recuperar acesso. O titular de uma conta poderá solicitar recuperação por um canal previamente confirmado. Proposta pendente: mecanismo e prazo de validade. Critério candidato: após concluir a recuperação, a credencial anterior deixa de permitir acesso. Decisões pendentes: tratamento de sessões ativas e indisponibilidade do canal.

Use Dado/Quando/Então quando facilitar a avaliação; não o imponha a todo requisito. Critérios devem afirmar resultados observáveis e rejeições, não simplesmente repetir o enunciado. Inclua exceções e consequências persistidas quando relevantes.

## Casos de uso, domínio e acesso

Em casos de uso, registre atores, objetivo, gatilho, precondições, fluxo principal, alternativas, erros e pós-condições. Relacione os requisitos. Separe autenticação, autorização sobre a operação e autorização sobre o recurso.

No domínio, registre conceitos, relacionamentos, cardinalidades e invariantes relevantes. Não transforme automaticamente classes técnicas em conceitos de negócio. Para dados, esclareça obrigatoriedade, unicidade, ciclo de vida e retenção quando necessário.

Em uma matriz de acesso, relacione papel, ação, recurso e condição (por exemplo, apenas registros próprios). Marque permissões desconhecidas como pendentes; não presuma acesso por omissão.

## Diagramas proporcionais

Selecione diagramas para resolver dúvidas concretas. Mantenha fonte editável, legenda quando necessária e vínculo com IDs. Diferencie desenho conceitual de arquitetura implementada. Para estados, explicite transições válidas, guardas e estados finais; para sequência, inclua falhas e repetições quando alterarem as garantias do fluxo.

## Roadmap e decisões

Associe cada etapa a uma entrega útil e critérios de conclusão. Mantenha escopo aprovado separado de possibilidades futuras. Não trate uma lista de funcionalidades como cronograma estimado.

Para uma decisão, registre ID, data, questão, alternativas, decisão e responsável pela confirmação, justificativa, impacto e decisões substituídas. Um item pode permanecer proposto; registre a confirmação apenas quando houver evidência dela.

## Revisão para QA

Verifique se é possível derivar cenários normais, negativos, de limite, acesso, concorrência e recuperação conforme o risco. Documente invariantes e resultados esperados; não confunda uma futura sugestão de teste com teste executado. Uma matriz pode relacionar requisito, critério, cenário e evidência, deixando campos desconhecidos explícitos.
