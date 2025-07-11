# Guia para Compartilhar seu Primeiro Projeto no GitHub

Olá, futuro(a) colaborador(a)! Se você está lendo isto, provavelmente criou um projeto incrível no seu computador e agora quer mostrá-lo ao mundo, criar um portfólio ou simplesmente guardá-lo em um lugar seguro.

Este guia foi feito para você. Vamos passar, passo a passo, pelo processo de pegar um projeto do seu PC e publicá-lo no GitHub.

## O que são Git e GitHub? (A explicação rápida)

* **Git:** Pense no Git como uma "máquina do tempo" para o seu código, instalada no seu computador. Ele permite que você salve "fotos" (chamadas de *commits*) do seu projeto ao longo do tempo. Se algo der errado, você pode simplesmente voltar para uma "foto" anterior que funcionava.
* **GitHub:** É uma plataforma online, como uma rede social para projetos de código. Ele armazena seus projetos (chamados de *repositórios*) na nuvem, usando o Git. É no GitHub que a mágica da colaboração acontece.

---

## Passo a Passo: Do seu PC para o Mundo

Vamos dividir o processo em três partes.

### Parte 1: Preparando o Terreno (só precisa fazer uma vez)

1. **Crie uma conta no GitHub:** Acesse [github.com](https://github.com) e crie sua conta gratuita.
2. **Instale o Git:** Se você ainda não tem o Git, baixe e instale a partir do site oficial: [git-scm.com](https://git-scm.com/). A instalação é simples, basta seguir o assistente clicando em "Next".

### Parte 2: Criando um "Espaço Vazio" no GitHub

Agora que você tem uma conta, precisa criar um repositório online para receber seu projeto.

1. Faça login no GitHub.
2. No canto superior direito, clique no ícone de `+` e depois em **New repository**.
3. **Preencha os campos:**
    * **Repository name:** Dê um nome curto e descritivo para o seu projeto (ex: `meu-portfolio-web`).
    * **Description:** Escreva uma frase explicando o que seu projeto faz.
    * **Public / Private:** Escolha **Public** se quiser que todos vejam (ótimo para portfólio!).
    * **NÃO marque** a opção "Add a README file" por enquanto, pois vamos enviar o nosso próprio projeto.
4. Clique em **Create repository**.

O GitHub irá te mostrar uma página com alguns comandos. É a nossa "cola" para o próximo passo!

### Parte 3: Enviando seu Projeto para o GitHub

Agora vamos conectar a pasta do seu projeto no seu computador com o repositório que você acabou de criar no GitHub.

1. **Abra o terminal ou prompt de comando:**

    * No Windows, você pode usar o "Git Bash" (que foi instalado com o Git) ou o "Windows Terminal".
    * No macOS ou Linux, use o "Terminal".

2. **Navegue até a pasta do seu projeto:** Use o comando `cd` (change directory).

    ```bash
    # Exemplo: se seu projeto está na Área de Trabalho em uma pasta chamada "meu-site"
    cd Desktop/meu-site
    ```

3. **Execute os seguintes comandos, um por um.** Eles são baseados na "cola" que o GitHub te deu.

    ```bash
    # 1. Inicia o Git na sua pasta, transformando-a em um repositório local.
    git init

    # 2. Adiciona todos os arquivos do seu projeto para a "área de preparação".
    # O ponto "." significa "tudo nesta pasta".
    git add .

    # 3. Tira a primeira "foto" (commit) do seu projeto.
    # A mensagem é importante para você saber o que foi feito.
    git commit -m "Primeiro commit: versão inicial do projeto"

    # 4. Renomeia a branch principal para "main" (um padrão moderno).
    git branch -M main

    # 5. Conecta sua pasta local ao repositório remoto no GitHub.
    # Copie a URL do seu repositório (a que termina com .git).
    git remote add origin https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git

    # 6. Envia (push) seu código para o GitHub!
    git push -u origin main
    ```

**Pronto!** Atualize a página do seu repositório no GitHub. Seus arquivos estarão lá!

---

## Como Atualizar seu Projeto?

Agora que a conexão está feita, o processo para enviar atualizações é muito mais simples.

1. Faça as alterações que quiser no seu código.
2. No terminal, dentro da pasta do projeto, execute:

    ```bash
    # Adiciona as novas alterações
    git add .

    # Tira uma nova "foto" com uma mensagem do que você mudou
    git commit -m "feat: Adiciona seção de contato na página principal"

    # Envia as atualizações para o GitHub
    git push
    ```

É isso! Você acabou de aprender o fluxo essencial de trabalho com Git e GitHub.

### Próximos Passos

Quando você se sentir confortável com este fluxo, o próximo passo é aprender a colaborar em equipe. Para isso, nosso projeto tem um **[Guia de Colaboração](CONTRIBUTING.md)** que ensina sobre Branches e Pull Requests.

Parabéns por dar este passo importante na sua jornada como desenvolvedor(a)!