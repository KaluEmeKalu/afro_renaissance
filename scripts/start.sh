#!/bin/bash
set -e

echo "Running migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Creating superuser if not exists..."
python manage.py shell << EOF
from django.contrib.auth.models import User
if not User.objects.filter(username='${DJANGO_SUPERUSER_USERNAME}').exists():
    User.objects.create_superuser('${DJANGO_SUPERUSER_USERNAME}', '${DJANGO_SUPERUSER_EMAIL}', '${DJANGO_SUPERUSER_PASSWORD}')
    print('Superuser created successfully')
else:
    print('Superuser already exists')
EOF

echo "Starting Gunicorn..."
gunicorn afro_renaissance.wsgi:application --bind 0.0.0.0:$PORT --log-level debug --access-logfile - --error-logfile -