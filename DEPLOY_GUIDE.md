# Guia de Deploy no GitHub Pages com GitHub Actions

Este guia explica como automatizar a publicação da sua galeria de imagens no GitHub Pages. Usaremos o GitHub Actions para construir o site com Docker e fazer o deploy automaticamente sempre que você atualizar o branch `main`.

## Por que usar GitHub Actions?

* **Automação:** O site é gerado e publicado automaticamente. Você só precisa se preocupar em adicionar suas imagens.
* **Consistência:** O processo de build é sempre o mesmo, executado em um ambiente limpo.
* **Repositório Limpo:** Você não precisa fazer commit da pasta `pub` gerada. O branch `main` conterá apenas o código-fonte.

---

## Passo 1: Configurar o GitHub Pages no seu Repositório

Antes de criar a automação, você precisa dizer ao GitHub que o seu site será publicado a partir de uma Action.

1. Vá para a página principal do seu repositório no GitHub.
2. Clique em **Settings** (Configurações).
3. Na barra lateral esquerda, clique em **Pages**.
4. Na seção "Build and deployment", em **Source**, selecione **GitHub Actions**.

## Passo 2: Criar o Arquivo de Workflow

O GitHub Actions é configurado por um arquivo YAML dentro da pasta `.github/workflows/`.

1. Na raiz do seu projeto, crie uma pasta chamada `.github`.
2. Dentro de `.github`, crie outra pasta chamada `workflows`.
3. Dentro de `workflows`, crie um arquivo chamado `deploy.yml`.

A estrutura de pastas deve ficar assim:

    ```
    image-gallery/
    ├── .github/
    │   └── workflows/
    │       └── deploy.yml
    ├── src/
    ├── images/
    └── ...
    ```

## Passo 3: Conteúdo ao Arquivo `deploy.yml`

Segue um exemplo simples para realizar deploy automático no Github pages ao atualizar a branch `main`.
Verifique e adapte as suas necessidades!

    ```yaml
    name: Deploy to GitHub Pages

    on:
    # Executa em pushes direcionados ao branch padrão (main)
    push:
        branches: ["main"]

    # Permite que você execute este workflow manualmente na aba Actions
    workflow_dispatch:

    # Define as permissões do GITHUB_TOKEN para permitir o deploy no GitHub Pages
    permissions:
    contents: read
    pages: write
    id-token: write

    jobs:
    build-and-deploy:
        runs-on: ubuntu-latest
        steps:
        - name: Checkout repository
            uses: actions/checkout@v4

        - name: Build Docker image
            run: docker build -t image-gallery-generator .

        - name: Generate static site
            run: docker run --rm -v "$(pwd)/images:/app/images" -v "$(pwd)/pub:/app/pub" image-gallery-generator

        - name: Upload artifact
            uses: actions/upload-pages-artifact@v3
            with:
            path: './pub' # Faz o upload do conteúdo da pasta 'pub'

        - name: Deploy to GitHub Pages
            id: deployment
            uses: actions/deploy-pages@v4
    ```

## Passo 4: Fazer o Commit e Verificar

1. Adicione, faça o commit e envie os novos arquivos (`.github/workflows/deploy.yml` e `DEPLOY_GUIDE.md`) para o seu repositório no GitHub.

    ```bash
    git add .
    git commit -m "feat: Add GitHub Actions workflow for deployment"
    git push
    ```

2. Vá para a aba **Actions** no seu repositório. Você verá o workflow "Deploy to GitHub Pages" em execução.

3. Após a conclusão bem-sucedida, seu site estará disponível no endereço fornecido na seção **Settings > Pages**. Pode levar um ou dois minutos para que o site entre no ar pela primeira vez.

Pronto! A partir de agora, toda vez que você enviar uma alteração para o branch `main` (como adicionar novas imagens), o GitHub Actions irá automaticamente gerar e publicar a nova versão do seu site.
