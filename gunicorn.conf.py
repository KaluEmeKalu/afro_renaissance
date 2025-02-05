import os
import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).resolve().parent
sys.path.insert(0, str(project_root))

# Gunicorn configuration
bind = f"0.0.0.0:{os.getenv('PORT', '8080')}"
workers = 3
threads = 2
timeout = 120
capture_output = True
enable_stdio_inheritance = True
loglevel = "debug"
accesslog = "-"
errorlog = "-"

# Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "afro_renaissance.settings")

# Pre-load application
def on_starting(server):
    try:
        from django.core.wsgi import get_wsgi_application
        application = get_wsgi_application()
        server.log.info("Successfully loaded WSGI application")
    except Exception as e:
        server.log.error(f"Failed to load WSGI application: {e}")
        raise