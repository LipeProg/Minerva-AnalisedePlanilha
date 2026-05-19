import os
import sys
from pathlib import Path

from django.core.wsgi import get_wsgi_application

CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datadash.settings')

application = get_wsgi_application()
