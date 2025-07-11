# Como mover arquivos com segurança (e atualizar referências)

Uma das tarefas mais comuns durante a manutenção de um projeto é reorganizar arquivos e pastas. Fazer isso da maneira errada pode quebrar links e referências, causando bugs e frustração.

A regra de ouro é: **nunca mova ou renomeie arquivos usando o explorador de arquivos do seu sistema operacional**. Faça sempre a movimentação dentro do próprio VS Code.

## O Jeito Certo: Usando o VS Code

O VS Code possui uma funcionalidade de refatoração inteligente que detecta quando um arquivo é movido e se oferece para atualizar todos os caminhos que apontam para ele.

Siga estes passos:

1.**Use o Painel "Explorer"**: Na barra lateral esquerda do VS Code, localize o arquivo que você deseja mover.

2.**Arraste e Solte**: Clique no arquivo, segure e arraste-o para a nova pasta de destino.

3.**Confirme a Atualização**: Após soltar o arquivo, o VS Code exibirá uma notificação no canto inferior direito, perguntando se você deseja atualizar as referências para o arquivo movido.

    > **Clique em "Yes"** para que o VS Code analise seu projeto e atualize automaticamente todos os links.

### Dica de Ouro: Extensão Recomendada

Para garantir que essa funcionalidade funcione perfeitamente com arquivos Markdown (`.md`), é altamente recomendável ter a extensão **Markdown All in One** instalada. Ela aprimora a capacidade do VS Code de entender e gerenciar links dentro de seus documentos.

### Verificando as Mudanças

Após a refatoração, use a aba "Source Control" (Controle do Código-Fonte) do Git no VS Code. Você verá o arquivo movido e todos os outros arquivos que tiveram seus links internos alterados, permitindo que você revise tudo antes de fazer o commit.
