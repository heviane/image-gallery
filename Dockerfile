# Use uma imagem base oficial do Python.
# Usar 'slim' mantém a imagem final menor.
FROM python:3.10-slim-bookworm

# Atualiza os pacotes do sistema para corrigir vulnerabilidades
RUN apt-get update && apt-get upgrade -y && apt-get clean

# Define o diretório de trabalho dentro do contêiner.
WORKDIR /app

# Copia o diretório 'src' do host para o diretório de trabalho '/app' no contêiner.
COPY src/ ./src/

# Define o comando padrão a ser executado quando o contêiner iniciar.
# Isso irá executar o script do gerador.
CMD ["python", "src/generator.py"]

