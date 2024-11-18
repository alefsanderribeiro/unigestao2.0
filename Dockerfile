FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /app

# Instala dependências do sistema necessárias para Python e PostgreSQL
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia o arquivo de dependências
COPY requirements.txt /app/

# Instala dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do projeto
COPY . /app/

# Torna o script de inicialização executável
RUN chmod +x /app/scripts/entrypoint.sh

# Define a porta exposta
EXPOSE 8000

# Comando padrão para rodar o servidor Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi:application"]
