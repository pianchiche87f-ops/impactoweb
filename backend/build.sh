#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

# Crear superusuario automáticamente si no existe
python manage.py shell << 'EOF'
from django.contrib.auth.models import User
import os
username = os.environ.get('ADMIN_USER', 'admin')
email    = os.environ.get('ADMIN_EMAIL', 'admin@impactoweb.agency')
password = os.environ.get('ADMIN_PASSWORD', '')
if password and not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f'Superusuario "{username}" creado correctamente.')
else:
    print(f'Superusuario "{username}" ya existe o no se definió ADMIN_PASSWORD.')
EOF
