"""
WSGI config for afro_renaissance project.
"""

import os
import sys
from pathlib import Path

# Add the project directory to the sys.path
project_path = Path(__file__).resolve().parent
sys.path.insert(0, str(project_path))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'afro_renaissance.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()