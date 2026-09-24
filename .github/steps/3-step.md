## Step 3: Resolver issues com o Agent Mode e o GitHub MCP Server

Ótimo trabalho na pesquisa e ao encontrar uma possível oportunidade de colaboração.
Além de descobrir novas ideias para ajudar a organizar as atividades extracurriculares, fizemos tudo isso rapidamente.

Agora, vamos usar as ferramentas do nosso MCP server e o Copilot para fazer um pouco de triagem e colocar o trabalho em dia.

### :keyboard: Atividade: implemente facilmente uma issue importante

O backlog de issues está crescendo. Vamos finalmente resolver uma delas — mas qual merece nossa atenção primeiro?

1. Garanta que o painel **Copilot Chat** esteja aberto e o modo **Agent** selecionado. Confirme também que as ferramentas do MCP server continuam disponíveis.

1. Pergunte ao Copilot sobre as issues abertas neste repositório.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Quantas issues abertas existem no meu repositório?
   > ```

   > 🪧 **Observação:** confira se a ferramenta List Issues foi chamada com os parâmetros corretos.

1. Peça ao Copilot que resuma as issues importantes.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Nossa, são issues demais para mim! Busque a lista de issues,
   > revise as descrições e os comentários e escolha as 3 mais importantes.
   > ```

   <details>
   <summary> <b> 💡 Dica:</b> pré-autorizar o uso de ferramentas</summary><br/>

   Se o Copilot usa uma ferramenta com frequência, você pode conceder permissão de forma proativa para o restante da sessão de conversa.

   <img width="350" src="https://github.com/user-attachments/assets/d741191e-4d98-489d-92d2-f1069fd6c34e"/>

   </details>

1. Revise as issues sugeridas. Se o Copilot não deu uma recomendação específica, tente dar algum feedback para refinar os resultados.

1. Com a lista reduzida, peça ao Copilot que implemente uma issue. **A Mona não vai avaliar se as alterações funcionam, apenas que houve uma tentativa.**

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > #codebase Vamos fazer a primeira. Siga estes passos:
   > 1. Crie uma nova branch local para as nossas alterações.
   > 2. Faça as alterações e confirme comigo se estão corretas.
   > 3. Envie as alterações e crie um pull request.
   > ```

   > ⚠️ **Atenção:** sempre verifique as ações que o Copilot pede para executar, especialmente com as habilidades externas fornecidas por um MCP server, que provavelmente não têm opção de desfazer.

1. Assim que o pull request for criado, a Mona começará a conferir seu trabalho. Dê um tempinho a ela e acompanhe os comentários. Você verá a resposta dela com informações de progresso e o próximo passo!

<details>
<summary>Com dificuldades?</summary><br/>

- Se as ferramentas não estiverem sendo solicitadas, verifique se sua configuração de MCP está correta.
- Se o Copilot não conseguir obter resultados, confirme se você está usando o token deste Codespace ou um Personal Access Token (PAT) com as permissões adequadas. Por padrão, o token do codespace que estamos usando só tem acesso a este repositório.

</details>
