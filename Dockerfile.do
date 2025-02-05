# Use Python 3.11 slim image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=8080 \
    PYTHONPATH=/app

# Set work directory
WORKDIR /app

# Install system dependencies including Pillow requirements
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    python3-dev \
    zlib1g-dev \
    libjpeg-dev \
    libfreetype6-dev \
    liblcms2-dev \
    libwebp-dev \
    libopenjp2-7-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip and install build tools
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Create necessary directories
RUN mkdir -p staticfiles mediafiles

# Collect static files
RUN python manage.py collectstatic --noinput

# Run migrations
RUN python manage.py migrate --noinput

# Create a script to run the application
RUN echo '#!/bin/bash\n\
cd /app\n\
exec gunicorn --chdir /app afro_renaissance.wsgi:application \
    --bind 0.0.0.0:$PORT \
    --workers 3 \
    --threads 2 \
    --log-level debug \
    --access-logfile - \
    --error-logfile - \
    --capture-output \
    --enable-stdio-inheritance' > /app/run.sh \
    && chmod +x /app/run.sh

# Run the application
CMD ["/app/run.sh"]