# Modo administrador

## Problema

Estudantes estão removendo uns aos outros para liberar vaga para si mesmos nas atividades.

## Solução recomendada

Adicionar um ícone de usuário no canto superior direito. Ao clicar nele, deve aparecer um botão de login. Ao clicar no botão de login, deve abrir uma janela para informar usuário e senha.

- Apenas os professores (autenticados) podem inscrever e remover estudantes das atividades.

- Os estudantes (sem login) continuam podendo ver quem está inscrito.

- Não é preciso ter uma página de manutenção de contas. Os professores receberão senhas já definidas.

## Contexto

Como ainda não existe banco de dados, armazene os usuários e senhas dos professores em um arquivo `json` verificado pelo backend.
