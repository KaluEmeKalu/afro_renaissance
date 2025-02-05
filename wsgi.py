"""
WSGI config for afro_renaissance project.
"""

import os
import sys
from pathlib import Path

# Add the project root directory to Python path
current_dir = Path(__file__).resolve().parent
sys.path.append(str(current_dir))

from afro_renaissance.wsgi import application  # noqa

# This application object is used by any WSGI server configured to use this file
application = application