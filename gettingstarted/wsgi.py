import os
from django.core.wsgi import get_wsgi_application
import django
from django.core.management import call_command

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gettingstarted.settings")

# Inicjalizacja Django
django.setup()

# Automatyczne migracje przy starcie
try:
    call_command('migrate', interactive=False)
except Exception as e:
    print("Błąd przy migracjach:", e)

application = get_wsgi_application()
