#!/bin/bash

# Função para verificar falhas em comandos
check_command() {
    if [ $? -ne 0 ]; then
        echo "Erro na execução do comando: $1"
        exit 1
    fi
}

# Rodar migrações
echo "🟡 Rodando migrações..."
python manage.py migrate
check_command "migrações"

# Carregar dados dos fixtures
echo "🟡 Carregando fixtures de cbos..."
python manage.py loaddata cbos/fixtures/*.json
check_command "fixtures de cbos"

echo "🟡 Carregando fixtures de configurations..."
python manage.py loaddata configurations/fixtures/*.json
check_command "fixtures de configurations"

echo "🟡 Carregando fixtures de geography..."
python manage.py loaddata geography/fixtures/*.json
check_command "fixtures de geography"

# Verificar e criar superusuário se necessário
echo "🟡 Verificando e criando superusuário se necessário..."
if [ -z "${DJANGO_SUPERUSER_USERNAME}" ] || [ -z "${DJANGO_SUPERUSER_EMAIL}" ] || [ -z "${DJANGO_SUPERUSER_PASSWORD}" ]; then
    echo "Erro: variáveis de ambiente do superusuário não estão definidas."
    exit 1
fi

python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username="${DJANGO_SUPERUSER_USERNAME}").exists():
    User.objects.create_superuser(
        "${DJANGO_SUPERUSER_USERNAME}",
        "${DJANGO_SUPERUSER_EMAIL}",
        "${DJANGO_SUPERUSER_PASSWORD}"
    )
EOF
check_command "criação de superusuário"

# Criar grupo de usuário de nível 1
echo "🟡 Verificando e criando grupo de usuário de nível 1..."
python manage.py create_groups
check_command "criação do grupo de usuário de nível 1"

# Iniciar o servidor
echo "🟢 Iniciando servidor Django..."
python manage.py runserver 0.0.0.0:8000
check_command "início do servidor Django"
