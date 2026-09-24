## Step 1: Introdução ao MCP e preparação do ambiente

<img width="150" align="right" alt="copilot logo" src="https://github.com/user-attachments/assets/4d22496d-850b-4785-aafe-11cba03cd5f2" />

No exercício [Getting Started with GitHub Copilot](https://github.com/dev-pods/getting-started-with-github-copilot), conhecemos o site de atividades extracurriculares da Mergington High School, que permitia que estudantes se inscrevessem em eventos.

E agora temos um problema... mas... é um problema bom! Mais professores estão pedindo para usá-lo! 🎉

Nossos colegas professores têm muitas ideias, mas não conseguimos acompanhar todos os pedidos! 😮 Para resolver isso, vamos dar um upgrade no GitHub Copilot habilitando o Model Context Protocol (MCP). Mais especificamente, vamos adicionar o GitHub MCP server, que vai permitir um fluxo combinado de gerenciamento de issues e melhorias no site. 🧑‍🚀

Vamos começar!

### 📖 Teoria: o que é o Model Context Protocol (MCP)?

O [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) é frequentemente descrito como o "USB-C da IA" — um conector universal que permite ao GitHub Copilot (e a outras ferramentas de IA) interagir de forma fluida com outros serviços.

Basicamente, é uma maneira de descrever as capacidades e os requisitos de um serviço, para que ferramentas de IA consigam determinar facilmente quais métodos usar e informar os parâmetros corretos. Um MCP server é quem fornece essa interface.

```mermaid
graph LR
    A[Pessoa desenvolvedora] -->|Usa| B[GitHub Copilot]
    B -->|API unificada| MCP[Model Context Protocol]

    MCP <-->|API própria| C[(GitHub)]
    MCP <-->|API própria| D[(Slack)]
    MCP <-->|API própria| E[(Figma)]

    style B fill:#4CAF50,stroke:#333,stroke-width:2px

    subgraph "Menos troca de contexto, mais código"
        B
        MCP
        C
        D
        E

    end
```

### :keyboard: Atividade: conheça o seu ambiente

Antes de mergulhar no MCP, vamos iniciar nosso ambiente de desenvolvimento e relembrar a aplicação de atividades extracurriculares.

1. Clique com o botão direito no botão abaixo para abrir a página **Create Codespace** em uma nova aba. Use a configuração padrão.

   [![Abrir no GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/{{full_repo_name}}?quickstart=1)

1. Confirme que as extensões **Copilot Chat** e **Python** estão instaladas e habilitadas.

   <img width="300" alt="copilot extension for VS Code" src="https://github.com/user-attachments/assets/ef1ef984-17fc-4b20-a9a6-65a866def468" /><br/>
   <img width="300" alt="python extension for VS Code" src="https://github.com/user-attachments/assets/3040c0f5-1658-47e2-a439-20504a384f77" />

1. Verifique se a aplicação executa antes de qualquer modificação. Na barra lateral esquerda, selecione a aba **Run and Debug** e depois clique no ícone **Start Debugging**.

   <details>
   <summary>📸 Mostrar captura de tela</summary><br/>

   <img width="300" alt="run and debug" src="https://github.com/user-attachments/assets/50b27f2a-5eab-4827-9343-ab5bce62357e" />

   </details>

   <details>
   <summary>🤷 Com dificuldades?</summary><br/>

   Se a área **Run and Debug** estiver vazia, tente recarregar o VS Code: abra a paleta de comandos (`Ctrl`+`Shift`+`P`) e procure por `Developer: Reload Window`.

   <img width="300" alt="empty run and debug panel" src="https://github.com/user-attachments/assets/0dbf1407-3a97-401a-a630-f462697082d6" />

   </details>

1. Use a aba **Ports** para encontrar o endereço da página, abra-o e confirme que a aplicação está no ar.

   <details>
   <summary>📸 Mostrar captura de tela</summary><br/>

   <img width="350" alt="ports tab" src="https://github.com/user-attachments/assets/8d24d6b5-202d-4109-8174-2f0d1e4d8d44" />

   ![Captura de tela do WebApp da Mergington High School](https://github.com/user-attachments/assets/5cb88d53-d948-457e-9f4b-403d697fa93a)

   </details>

### :keyboard: Atividade: adicionar o GitHub MCP server

1. Dentro do seu codespace, abra o painel **Copilot Chat** e confirme que o modo **Agent** está selecionado.

   <img width="200" alt="image" src="https://github.com/user-attachments/assets/201e08ab-14a0-48bf-824e-ba4f8f43f8ab" />

   <details>
   <summary>O modo Agent não aparece?</summary><br/>

   - Verifique se o VS Code está pelo menos na versão `v1.99.0`.
   - Verifique se a extensão do Copilot está pelo menos na versão `v1.296.0`.
   - Confira se o modo Agent está habilitado nas suas [configurações de usuário ou de workspace](https://code.visualstudio.com/docs/configure/settings#_workspace-settings).

      <img width="300" alt="image" src="https://github.com/user-attachments/assets/407a79dd-707e-471b-b56b-1938aece4ad8" />

   </details>

1. Dentro do seu codespace, navegue até a pasta `.vscode` e crie um novo arquivo chamado `mcp.json`. Cole o seguinte conteúdo:

   📄 **.vscode/mcp.json**

   ```json
   {
     "servers": {
       "github": {
         "type": "http",
         "url": "https://api.githubcopilot.com/mcp/"
       }
     }
   }
   ```

1. No arquivo `.vscode/mcp.json`, clique no botão **Start** e aceite o prompt para autenticar com o GitHub. Com isso, o GitHub Copilot acabou de ser informado sobre as capacidades do MCP server.

   <img width="350" alt="mcp.json file showing start button" src="https://github.com/user-attachments/assets/15a3d885-1c13-40b4-8d59-87b478ddd8a0" />

   <img width="350" alt="allow authentication prompt" src="https://github.com/user-attachments/assets/f5ec128d-9924-454b-8ab4-3f43ebc83cfc" /><br/>

   <img width="350" alt="mcp.json file showing running server" src="https://github.com/user-attachments/assets/c413c52d-94dc-429f-91e0-3486141908b9" />

1. No painel lateral do Copilot, clique no **ícone 🛠️** para ver as capacidades adicionais.

   <img width="350" alt="image" src="https://github.com/user-attachments/assets/b1be8b80-c69c-4da5-9aea-4bbaa1c6de10" />

   <img width="350" alt="image" src="https://github.com/user-attachments/assets/99178d1b-adbe-4cf4-ab9c-3a4d29918a13" />

1. Faça **commit** e **push** do arquivo `.vscode/mcp.json` para a branch `main`.

   > 🪧 **Observação:** fazer push diretamente na `main` não é uma prática recomendada. Aqui é apenas para simplificar o exercício.

1. Agora que a configuração do seu MCP server foi enviada para o GitHub, a Mona já deve estar conferindo seu trabalho. Dê um tempinho a ela e acompanhe os comentários. Você verá a resposta dela com informações de progresso e a próxima lição.

> [!NOTE]
> Os próximos passos envolvem a criação de issues no GitHub. Se quiser evitar e-mails de notificação, você pode deixar de acompanhar (unwatch) o repositório.

<details>
<summary>Com dificuldades?</summary><br/>

Confirme se:

- Seu arquivo `.vscode/mcp.json` está parecido com o exemplo fornecido.
- Você enviou (push) as alterações para a branch `main`.

</details>
