# Como descartar alterações em um arquivo no Git

Às vezes, enquanto trabalhamos, modificamos um arquivo por engano e precisamos que ele volte a ser exatamente como era no último commit. Um exemplo comum é o `package-lock.json`, que pode ser alterado automaticamente ao rodar comandos como `npm install`.

Felizmente, o Git torna essa tarefa muito simples.

## Cenário: Você modificou um arquivo, mas ainda não commitou

Esta é a situação mais comum. Para descartar as alterações e restaurar o arquivo para a versão do último commit, você tem duas opções.

### 1. Usando `git restore` (Método Recomendado)

Este é o comando moderno, claro e feito exatamente para isso.

```bash
# Sintaxe: git restore <caminho/para/o/arquivo>
git restore package-lock.json
```

**O que ele faz?** Ele simplesmente descarta todas as suas alterações locais no arquivo, fazendo-o voltar à sua última versão salva no histórico do Git.

### 2. Usando `git checkout --` (Método Clássico)

Esta é a forma mais antiga de fazer a mesma coisa e ainda é muito usada.

```bash
# Sintaxe: git checkout -- <caminho/para/o/arquivo>
git checkout -- package-lock.json
```

O resultado é o mesmo do `git restore`. O `--` é importante para garantir que o Git entenda que você está falando de um arquivo, e não tentando trocar de branch.

---

## Cenário: Você já commitou a alteração por engano

Se você já salvou a alteração com `git commit`, o processo é diferente. Não podemos simplesmente descartar a mudança, pois ela já faz parte do histórico. A forma correta e segura é **reverter o commit**.

O comando `git revert` cria um **novo commit** que desfaz exatamente o que o commit anterior fez. É a forma mais segura de corrigir um erro no histórico, especialmente em projetos colaborativos.

```bash
# 1. Encontre o hash do commit que você quer reverter
git log --oneline

# 2. Use o hash para reverter o commit
git revert <hash-do-commit-errado>
```
