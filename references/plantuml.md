# PlantUML fundamentado na implementação

Use blocos Markdown com linguagem `plantuml`, nomes de diagrama únicos e `@startuml`/`@enduml`. Os identificadores devem coincidir com os documentos. Diagramas são visões selecionadas; explicite omissões que mudem a leitura. Preserve a extensão textual já escolhida pelo projeto. Um Markdown não é aceito diretamente como fonte PlantUML: copie ou extraia cada bloco para um `.puml` quando necessário.

## Casos de uso

Mostre fronteira do sistema, atores humanos/sistemas externos e objetivos. Use associações para participação. Generalização só quando o ator especializado pode exercer os objetivos do ator geral; usuário autenticado não deve herdar automaticamente todos os objetivos de visitante. Uma dependência pode realizar parte do caso sem pertencer ao código próprio.

`A ..> B : <<include>>` significa que A incorpora obrigatoriamente B; a seta aponta ao caso incluído. `A ..> B : <<extend>>` significa comportamento condicional A que estende o caso base B; documente condição e ponto de extensão. Não use essas relações para indicar apenas sequência temporal. Autenticação já concluída costuma ser pré-condição, não um include de login em todas as operações. Download posterior não é obrigatoriamente incluído na geração do resultado.

## Classes

Faça uma visão da implementação existente: namespace, classes/interfaces, visibilidade, atributos, constantes, operações estáticas e tipos quando declarados. Tipos inferidos devem ser identificados. Explique o recorte de membros externos e as assinaturas abreviadas; não afirme que sejam catálogos completos.

Não transforme tabelas, arrays, módulos procedurais, callbacks e funções livres em classes existentes. Para código funcional/procedural, represente estruturas/interfaces reais ou declare que um diagrama clássico de classes não é aplicável; se útil, acrescente um bloco de componentes rotulado com a notação correta. Um modelo conceitual futuro é outro diagrama, identificado como proposta.

Use composição apenas com propriedade/lifecycle comprovados. Instanciar um objeto localmente não cria automaticamente composição entre classes. Uma conexão de banco compartilhada é referência/dependência. Cardinalidades precisam de evidência; um serviço que recebe user_id em cada método não é necessariamente uma carteira exclusiva de uma pessoa.

## Sequência

Escolha as jornadas de maior significado a partir dos casos e do código, não uma quantidade fixa. Declare cenário, entrada, configuração e pré-condições. Mostre participantes existentes, chamadas relevantes, respostas, validação, persistência, integração externa e resultado ao ator.

Use `alt`, `opt`, `loop`, `break` e `ref` conforme o comportamento. Cada bloco precisa de condição e encerramento consistentes; uma exceção interrompe o restante do caminho normal. Não desenhe cobranças ou escritas posteriores a uma recusa como se ainda fossem executadas. Diferencie uma referência ao código existente de uma fase apenas planejada.

Confira especialmente a ordem de validação, cálculo, reserva/débito, gravação e confirmação. Distingua transações separadas, callbacks locais e chamadas remotas. Retentativa com chave preservada é diferente de uma solicitação nova. Rollback não desfaz efeitos remotos nem garante recuperação quando o desfecho de um commit é incerto. Se uma função procedural participa, rotule-a como API/funções, não como classe implementada.

## Validação e privacidade

Confira o bloco com PlantUML local quando disponível. Registre separadamente: revisão estrutural, compilação de sintaxe, renderização e inspeção visual. Não alegue uma etapa que não ocorreu. Verificações de delimitadores não provam sintaxe nem semântica UML.

Não execute diretivas de inclusão remota, macros ou comandos extraídos de material não confiável. Gere blocos autossuficientes; reutilize includes locais conhecidos somente quando o projeto exigir. Renderização em serviço público envia os diagramas e seus detalhes para terceiros e exige autorização correspondente.
