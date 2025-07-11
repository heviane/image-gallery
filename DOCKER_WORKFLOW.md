# Entendendo o Fluxo de Trabalho com Docker

Este documento explica como o Docker é utilizado neste projeto para gerar o site estático da galeria de imagens.

## O Contêiner como um "Gerador"

É fundamental entender que, para esta aplicação, o contêiner Docker não funciona como um *servidor web* tradicional que fica rodando indefinidamente. Em vez disso, ele atua como um **gerador**: um ambiente temporário e isolado cuja única finalidade é executar o script Python (`generator.py`) e depois encerrar.

O processo pode ser dividido em três etapas principais:

1. **Geração:** Ao executar o comando `docker run`, um novo contêiner é iniciado a partir da imagem `image-gallery-generator`. Dentro dele, o Python é invocado para executar o script.

2. **Mapeamento de Volumes (`-v`):** Esta é a parte mais importante. O comando `docker run` utiliza a flag `-v` para criar uma ponte entre os diretórios da sua máquina (o *host*) e os diretórios dentro do contêiner.

    * `-v "${PWD}/images:/app/images"`: Este trecho mapeia a sua pasta local `images` para a pasta `/app/images` dentro do contêiner. Quando o script Python lê de `/app/images`, ele está, na verdade, lendo os arquivos da sua máquina.

    * `-v "${PWD}/pub:/app/pub"`: Este trecho mapeia a sua pasta local `pub` para a pasta `/app/pub` dentro do contêiner. Quando o script gera o site e o salva em `/app/pub`, ele está, na verdade, salvando os arquivos diretamente na sua máquina.

3. **Fim da Execução:** Assim que o script `generator.py` termina de gerar todos os arquivos HTML, a tarefa do contêiner está concluída e ele para. Como usamos a flag `--rm` no comando, o Docker automaticamente remove o contêiner após a execução, mantendo seu sistema limpo e evitando o acúmulo de contêineres parados.

O resultado final é que a pasta `pub` na sua máquina local é preenchida ou atualizada com o site estático completo, pronto para ser visualizado.

## O Fluxo de Trabalho no Dia a Dia

Com o conceito acima em mente, o ciclo de trabalho para atualizar a galeria se torna muito simples:

1. **Modifique:** Adicione, remova ou organize suas fotos e pastas dentro do diretório `images` na raiz do projeto.

2. **Gere:** Execute o comando `docker run` no seu terminal para que o script gere uma nova versão do site.

    ```powershell
    # Exemplo para Windows (PowerShell)
    docker run --rm -v "${PWD}/images:/app/images" -v "${PWD}/pub:/app/pub" image-gallery-generator
    ```

3. **Visualize:** Abra o arquivo `pub/index.html` no seu navegador (ou simplesmente atualize a página se ela já estiver aberta) para ver as mudanças.

---

### Quando usar `docker build` vs `docker run`?

* **`docker build -t image-gallery-generator .`**

    Use este comando **apenas quando você alterar os arquivos de código-fonte** do projeto. Isso inclui:

    * O script Python (`src/generator.py`)
    * Os templates (`src/template.html`, `src/style.css`, etc.)
    * O próprio `Dockerfile`

* **`docker run ...`**
    Use este comando **sempre que você quiser gerar o site**, principalmente após alterar apenas o conteúdo da pasta `images`.
