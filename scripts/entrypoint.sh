#!/bin/bash

# Exit on error
set -e

# Set Python path
export PYTHONPATH=/app:$PYTHONPATH

# Enable debug output
set -x

# Wait for PostgreSQL to be ready
echo "Waiting for PostgreSQL..."
while ! nc -z db 5432; do
  sleep 0.1
done
echo "PostgreSQL is ready!"

# Create database migrations
echo "Creating database migrations..."
python manage.py makemigrations

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Create static files directory if it doesn't exist
mkdir -p staticfiles
mkdir -p mediafiles

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Initialize database with manifesto content if needed
echo "Checking if initial data needs to be loaded..."
python scripts/init_data.py

# Start Gunicorn with debug logging
echo "Starting Gunicorn..."
cd /app && exec gunicorn \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --threads 2 \
    --timeout 60 \
    --reload \
    --log-level debug \
    --access-logfile - \
    --error-logfile - \
    --capture-output \
    afro_renaissance.wsgi:application