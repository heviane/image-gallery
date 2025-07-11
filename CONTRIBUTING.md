# Guia de Colaboração

Olá e seja bem-vindo(a) ao projeto! Ficamos felizes com seu interesse em contribuir.

Para garantir a qualidade do código e a estabilidade do ambiente de produção (publicado no GitHub Pages), seguimos um fluxo de trabalho organizado. Este documento descreve os passos necessários para colaborar.

## Sumário

- [Fluxo de Trabalho de Contribuição](#fluxo-de-trabalho-de-contribuição)
- [Reportando Bugs e Sugerindo Funcionalidades](#reportando-bugs-e-sugerindo-funcionalidades)
- [Configurando o Repositório (Para Administradores)](#configurando-o-repositório-para-administradores)

---

## Fluxo de Trabalho de Contribuição

Todo o desenvolvimento deve ser feito em branches separadas, nunca diretamente na `main`. As alterações só são integradas à `main` através de **Pull Requests (PRs)**, que são revisados e testados automaticamente.

### Passo 1: Crie uma Branch

Antes de começar a codificar, crie uma nova branch a partir da `main`. Use um nome descritivo, prefixado com `feature/`, `fix/`, `docs/`, etc.

```bash
# 1. Certifique-se de que sua branch main local está atualizada
git checkout main
git pull origin main

# 2. Crie sua nova branch
git checkout -b feature/nome-da-sua-funcionalidade
```

### Passo 2: Desenvolva e Faça Commits

Faça suas alterações na nova branch. Crie commits pequenos e atômicos com mensagens claras.

```bash
# Adicione os arquivos que você modificou
git add .

# Faça o commit das suas alterações
git commit -m "feat: Adiciona a funcionalidade X na página de contato"
```

### Passo 3: Abra um Pull Request (PR)

Quando seu trabalho estiver pronto para revisão, envie sua branch para o repositório remoto e abra um Pull Request.

```bash
# Envie sua branch para o GitHub
git push origin feature/nome-da-sua-funcionalidade
```

Acesse a página do repositório no GitHub. Você verá um aviso para criar um Pull Request a partir da sua nova branch. Clique nele e preencha o formulário do PR:

- **Título:** Um resumo conciso das suas alterações.
- **Descrição:** Detalhe o que foi feito, por que foi feito e como os revisores podem testar suas alterações.

### Passo 4: Revisão de Código e Testes Automáticos

Ao abrir o PR, o GitHub Actions será acionado automaticamente para:

1. **Construir o projeto (`build`):** Garante que seu código não quebrou o processo de build.
2. **Rodar testes (se houver):** Valida se as funcionalidades existentes continuam funcionando.

Outros desenvolvedores irão revisar seu código, deixar comentários e sugestões. Fique atento(a) às notificações para responder e fazer os ajustes necessários.

### Passo 5: Merge e Deploy Automático

Após a aprovação do PR e a passagem de todos os testes automáticos, um administrador irá fazer o "merge" das suas alterações na branch `main`.

**Este merge na `main` é o gatilho que inicia o deploy automático para o GitHub Pages.** Em poucos minutos, suas alterações estarão no ar!

---

## Reportando Bugs e Sugerindo Funcionalidades

Utilizamos as **Issues do GitHub** para rastrear bugs e novas funcionalidades.

Antes de criar uma nova Issue:

- **Verifique se já não existe uma Issue similar.** Se existir, participe da discussão em vez de criar uma duplicata.
- Para **reportar um bug**, use o template "Relatório de Bug" e forneça o máximo de detalhes possível.
- Para **sugerir uma funcionalidade**, use o template "Solicitação de Funcionalidade" e descreva claramente sua ideia e o problema que ela resolve.

---

## Configurando o Repositório (Para Administradores)

Para forçar o cumprimento deste fluxo de trabalho, é crucial proteger a branch `main`. Isso impede pushes diretos e garante que todas as alterações passem pelo processo de Pull Request.

Siga estes passos:

1. No seu repositório, vá para **Settings** (Configurações).
2. No menu lateral, clique em **Branches**.
3. Clique em **Add branch protection rule**.
4. Em **Branch name pattern**, digite `main`.
5. Marque a opção **Require a pull request before merging**.
    - Isso força o uso de PRs para qualquer alteração na `main`.
6. Marque a opção **Require status checks to pass before merging**.
    - Isso impede o merge de um PR se o workflow do GitHub Actions falhar.
    - Na caixa de busca que aparecer, procure e selecione o nome do seu job de verificação (neste caso, `build`).
7. **(Recomendado)** Marque **Require approvals** e defina o número de aprovações necessárias (geralmente `1`).
8. Clique em **Create** para salvar a regra.

Pronto! Seu repositório agora está configurado para um fluxo de colaboração seguro e organizado.
