# 🤝 Guia de Contribuição

Olá! Ficamos muito felizes com seu interesse em contribuir com o **Gerador de Galeria de Imagens**! 🎉

Toda contribuição, seja um relatório de bug, uma nova funcionalidade, uma melhoria na documentação ou qualquer outra ideia, é muito bem-vinda e apreciada.

Para garantir que o processo seja claro e eficiente para todos, criamos este guia.

## 📜 Código de Conduta

Antes de mais nada, por favor, leia nosso **[Código de Conduta](./CODE_OF_CONDUCT.md)**. Esperamos que todos os participantes da comunidade sigam estas diretrizes para garantir um ambiente respeitoso e colaborativo para todos.

## 🚀 Como Começar

Você pode contribuir de várias maneiras:

* **🐞 Relatando Bugs:** Encontrou um problema? Nos informe abrindo uma [issue de bug](https://github.com/heviane/image-gallery/issues/new?template=bug_report.md).
* **✨ Sugerindo Funcionalidades:** Tem uma ideia para melhorar o projeto? Adoraríamos ouvir! Abra uma [solicitação de funcionalidade](https://github.com/heviane/image-gallery/issues/new?template=feature_request.md).
* **📝 Melhorando a Documentação:** Viu um erro de digitação ou uma seção que poderia ser mais clara? Sinta-se à vontade para propor uma alteração.
* **💻 Escrevendo Código:** Se você quer colocar a mão na massa, siga os passos abaixo.

## 🛠️ Fluxo de Trabalho para Contribuição de Código

Se você está pronto para enviar seu primeiro Pull Request, aqui está o fluxo de trabalho que seguimos.

### 1. Prepare o Ambiente

* **Faça um Fork:** Clique no botão "Fork" no canto superior direito desta página para criar uma cópia do repositório na sua conta do GitHub.
* **Clone o seu Fork:**

```bash
git clone https://github.com/SEU-USUARIO/image-gallery.git
cd image-gallery
```

* **Configure o Ambiente Local:** Siga as instruções do `README.md` para instalar as dependências e rodar o projeto (seja com **Python** ou **Docker**).

### 2. Crie uma Branch

Crie uma nova branch para trabalhar na sua funcionalidade ou correção. Use um nome descritivo.

```bash
# Para uma nova funcionalidade
git checkout -b feat/nome-da-funcionalidade

# Para uma correção de bug
git checkout -b fix/descricao-do-bug
```

### 3. Faça suas Alterações e Commits

* **Escreva o código:** Faça as alterações que você propôs.
* **Siga o Estilo do Código:** Este projeto utiliza o formatador `black` para garantir um estilo de código Python consistente. Se você usa o VS Code, as configurações do projeto (`.vscode/settings.json`) já sugerem a extensão e formatam o código ao salvar.
* **Faça o Commit:** Adicione suas alterações e crie um commit com uma mensagem clara e concisa.

```bash
git add .
git commit -m "feat: Adiciona suporte para legendas nas imagens"
```

### 4. Envie o Pull Request (PR)

* **Envie sua Branch:** Faça o push da sua branch para o seu fork no GitHub.

```bash
git push origin feat/nome-da-funcionalidade
```

* **Abra o Pull Request:** Vá para o repositório original e você verá um botão para criar um Pull Request a partir da sua branch.
* **Preencha o Template:** Preencha o template do Pull Request com o máximo de detalhes possível. Isso nos ajuda a entender e revisar sua contribuição mais rapidamente.

Depois de enviar o PR, a nossa integração contínua (GitHub Actions) será executada. Um mantenedor do projeto irá revisar seu código e fornecer feedback.

Obrigado por sua contribuição! ❤️
