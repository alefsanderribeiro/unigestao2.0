#!/bin/bash

# Rodar migrações
echo "Rodando migrações..."
python manage.py migrate

# Coletar arquivos estáticos
echo "🟡 Coletando arquivos estáticos..."
python manage.py collectstatic --noinput

# Carregar dados dos fixtures
echo "🟡 Carregando fixtures de cbos..."
python manage.py loaddata cbos/fixtures/*.json
echo "🟡 Carregando fixtures de configurations..."
python manage.py loaddata configurations/fixtures/*.json
echo "🟡 Carregando fixtures de geography..."
python manage.py loaddata geography/fixtures/*.json

# Criar superusuário se não existir
echo "Verificando e criando superusuário se necessário..."
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

# Iniciar o servidor
echo "🟢 Iniciando servidor Django..."
python manage.py runserver 0.0.0.0:8000
