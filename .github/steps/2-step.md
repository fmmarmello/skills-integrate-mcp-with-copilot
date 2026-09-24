## Step 2: Agent Mode e um MCP server para o GitHub

Ótimo trabalho! Você acabou de conectar seu primeiro MCP server ao GitHub Copilot! 🎉

🚨 Os professores andaram ocupados abrindo novas issues no seu repositório com bugs e pedidos de funcionalidades! [Dê uma olhada](https://github.com/{{full_repo_name}}/issues) — quantas boas ideias!

É melhor analisarmos tudo isso e começarmos a pesquisar outras melhorias. Felizmente, com um MCP server para o GitHub, fazer a triagem e até pesquisar para sair na frente vai ser bem rápido! 🕵️

### 📖 Teoria: como funciona a chamada de ferramentas do MCP no Agent Mode

Agora que temos o GitHub MCP conectado, vamos ver como o **agent mode** realmente usa essas ferramentas externas.

A cada prompt que você envia, o Copilot também inclui o catálogo (lista + schema) das ferramentas disponíveis. Com isso, o Copilot consegue planejar e decidir:

- Alguma ferramenta é necessária para essa solicitação?
- Qual ou quais ferramentas melhor atendem à intenção?
- Quais argumentos (conforme o input schema de cada ferramenta) devem ser passados?

Em seguida, o Copilot executa a(s) chamada(s) de ferramenta escolhida(s) e devolve os resultados ao LLM.

![Diagrama de fluxo ilustrando como uma pessoa interage com o Copilot Agent Mode](https://github.blog/wp-content/uploads/2025/05/how-it-works.png)

> [!TIP]
> Você também pode sugerir explicitamente que o Copilot chame uma ferramenta específica incluindo `#<tool_name>` no seu prompt (por exemplo, `#create_pull_request`, `#codebase`).

A partir daqui, o Copilot pode usar um conjunto de ferramentas integradas ao GitHub para fazer muito mais do que apenas ler ou editar código no seu repositório. Veja algumas coisas que você pode pedir:

- Descobrir projetos públicos semelhantes para se inspirar.
- Pesquisar issues considerando descrição, comentários e reações.
- Transformar as novas ideias de que você gostou em issues imediatamente, para não perdê-las.
- Buscar uma issue, fazer alterações em uma branch e abrir um pull request.

Legal, né?! Agora vamos colocar em prática! 👩‍🚀

### :keyboard: Atividade: encontre e registre ideias rapidamente

Vamos colocar o GitHub MCP server para trabalhar pesquisando, comparando e registrando ideias de melhorias!

1. Feche todos os arquivos abertos no seu codespace. Isso ajuda a reduzir contexto desnecessário.

1. Garanta que o painel **Copilot Chat** esteja aberto e o modo **Agent** selecionado. Confirme também que as ferramentas do MCP server continuam disponíveis.

1. Peça ao Copilot para pesquisar no GitHub projetos semelhantes a este.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Pesquise outros repositórios para organizar atividades extracurriculares
   > ```

1. Quando uma ferramenta MCP for necessária, o Copilot pode pedir permissão. **Revise a solicitação** e ajuste se preciso, depois clique em **Continue**.

   <img width="250" alt="request permission dialog" src="https://github.com/user-attachments/assets/229473af-c206-47a4-b356-943b9c9bd946" />

1. Peça ao Copilot que descreva um dos projetos. Explore até encontrar algo de que você goste.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Analise o código da 3ª opção e me dê uma descrição detalhada das funcionalidades.
   > ```

1. Use o Copilot para comparar e gerar ideias de melhorias.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Compare essas funcionalidades com as do nosso projeto. Quais seriam novidade?
   > ```

1. Boa! Agora vamos pedir ao Copilot que crie issues para guardar essas ideias.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Gostei. Vamos criar issues para essas ideias no meu repositório.
   > ```

1. O Copilot vai pedir permissão para criar issues no seu repositório. Clique em **Continue** para cada nova issue. Lembrete: **revise a solicitação** antes de executar.

   <img width="250" alt="request permission dialog" src="https://github.com/user-attachments/assets/52635294-950a-4168-b71e-498eb769f3af" />

1. Como já terminamos a pesquisa, vamos encerrar esta sessão de chat para limpar o contexto. No topo do painel **Copilot Chat**, clique no ícone **New Chat** (sinal de mais).

1. Com as novas issues criadas, a Mona já deve estar conferindo seu trabalho. Dê um tempinho a ela e acompanhe os comentários. Você verá a resposta dela com informações de progresso e a próxima lição.

> [!NOTE]
> O cenário do Model Context Protocol (MCP) evolui rapidamente. Muitos servidores, incluindo o [GitHub MCP server oficial](https://github.com/github/github-mcp-server), estão em desenvolvimento ativo e ainda não têm paridade total com suas APIs estáveis.
