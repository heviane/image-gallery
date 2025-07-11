# 🖼️ Gerador de Galeria de Imagens Estática

Um script Python que gera automaticamente um website estático, navegável e responsivo a partir de uma simples estrutura de pastas e imagens. Ideal para portfólios, álbuns de fotos ou para organizar e visualizar assets de projetos.

---

## ✨ Funcionalidades

* **Geração Automática:** Cria páginas HTML a partir da estrutura de pastas em `images/`.
* **Navegação Recursiva:** Suporta subdiretórios ilimitados, com breadcrumbs para fácil navegação.
* **Responsivo:** Template moderno e limpo que se adapta a desktops e dispositivos móveis.
* **Zero Dependências (com Docker):** O uso do Docker elimina a necessidade de instalar Python ou qualquer outra dependência na sua máquina.
* **Leve e Rápido:** Por ser 100% estático, o site gerado é extremamente rápido e pode ser hospedado em qualquer lugar (GitHub Pages, Netlify, etc.).

> **Quer publicar seu site online?** Confira nosso [**Guia de Deploy no GitHub Pages**](./docs/github/DEPLOY_GUIDE.md).

## 🚀 Como Utilizar

O fluxo de trabalho é simples: você organiza suas imagens na pasta `images/` e executa um único comando para gerar ou atualizar o site na pasta `pub/`.

### Pré-requisitos

Você pode escolher um dos dois métodos abaixo. **O método com Docker é o recomendado** por sua simplicidade e portabilidade.

* **Método 1 (Recomendado):** Docker instalado e em execução.
* **Método 2 (Local):** Python 3.8+ instalado.

### Passo a Passo

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/heviane/image-gallery.git
    cd image-gallery
    ```

2. **Adicione suas imagens:** Crie a pasta `images/` na raiz do projeto (se ela não existir) e organize suas fotos e subpastas dentro dela.

3. **Gere o site:**

   #### Opção A: Com Docker (Recomendado)

    Primeiro, construa a imagem Docker (só precisa fazer isso uma vez ou quando o código-fonte for alterado):

    ```bash
    docker build -t image-gallery-generator .
    ```

    Depois, execute o contêiner para gerar o site. Escolha o comando para o seu sistema operacional:

    * **Linux ou macOS:**

        ```bash
        docker run --rm -v "$(pwd)/images:/app/images" -v "$(pwd)/pub:/app/pub" image-gallery-generator
        ```

    * **Windows (PowerShell):**

        ```powershell
        docker run --rm -v "${PWD}/images:/app/images" -v "${PWD}/pub:/app/pub" image-gallery-generator
        ```

   #### Opção B: Com Python Localmente

    Execute o script diretamente:

    ```bash
    python src/generator.py
    ```

4. **Visualize o resultado:** Abra o arquivo `pub/index.html` no seu navegador para ver sua galeria!

## 🤝 Como Contribuir

Contribuições são muito bem-vindas! Se você tem ideias para novas funcionalidades, melhorias ou encontrou um bug, sinta-se à vontade para colaborar.

Para garantir que o processo seja claro e organizado para todos, criamos um guia de contribuição. Por favor, leia o nosso **[Guia de Colaboração](CONTRIBUTING.md)** antes de começar.

> **É novo(a) no GitHub?** Se você está começando e quer aprender como compartilhar um projeto, confira nosso **[Guia para Iniciantes](./docs/github/getting-started-guide.md)**.

## 📜 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

---

*Este README foi gerado com a ajuda do Gemini Code Assist.*
