# Tipos de Documentação: Desenvolvedores vs. Usuários Finais

Separar a documentação de acordo com o público-alvo é uma das práticas mais importantes para a saúde e a escalabilidade de um projeto de software.

A regra fundamental é:

 > Documentação para **desenvolvedores** vive com o código.
 > Documentação para **usuários** vive com o produto.

## 1. Documentação para Desenvolvedores (Developer Docs)

Esta documentação é **técnica** e seu objetivo é ajudar outros desenvolvedores (ou você mesmo no futuro) a entender, manter e contribuir para o projeto.

* **Público-alvo**: Engenheiros de software, DevOps, QAs.
* **Conteúdo Típico**: Guias de arquitetura, decisões de design, instruções de setup do ambiente, guias de contribuição (`CONTRIBUTING.md`), padrões de código, documentação de API e guias de workflow.
* **Localização**: **Dentro do repositório do código-fonte**, na pasta `docs/`.
* **Por quê?**:
  * **Versionamento**: A documentação evolui junto com o código. Uma mudança na arquitetura pode ser documentada na mesma Pull Request, mantendo tudo sincronizado.
  * **Acessibilidade**: Qualquer pessoa que clona o repositório tem acesso imediato à documentação.
  * **Cultura "Docs as Code"**: Tratar a documentação como código incentiva os desenvolvedores a mantê-la atualizada.

## 2. Documentação para Usuários Finais (User Docs)

Esta documentação é **funcional** e seu objetivo é ensinar os usuários a extrair o máximo de valor do seu software.

* **Público-alvo**: O cliente final, que não tem conhecimento técnico.
* **Conteúdo Típico**: Guias de "como fazer" (how-to), tutoriais, FAQs, manuais de funcionalidades, notas de release (com foco no usuário).
* **Localização**: **Fora do repositório principal**, geralmente hospedada em uma plataforma dedicada (um site de ajuda, uma knowledge base, etc.).
* **Por quê?**:
  * **Experiência do Usuário**: Usuários precisam de uma interface amigável, com busca eficiente e navegação fácil, algo que um repositório Git não oferece.
  * **Acessibilidade**: Deve ser publicamente acessível via web, sem a necessidade de acessar o GitHub ou clonar um projeto.

### Tabela Resumo

| Característica  | Documentação para Desenvolvedores         | Documentação para Usuários Finais            |
| :---            | :---                                      | :---                                         |
| **Objetivo**    | Explicar **como o código funciona**       | Explicar **como usar o produto**             |
| **Público**     | Técnico (Desenvolvedores)                 | Não-técnico (Clientes)                       |
| **Localização** | Dentro do repositório do código           | Site/Plataforma externa                      |
| **Formato**     | Markdown (`.md`)                          | Site HTML, PDF, Plataforma SaaS              |
| **Exemplo**     | `CONTRIBUTING.md`, `docs/architecture.md` | `support.meusite.com`, `docs.meuproduto.com` |
