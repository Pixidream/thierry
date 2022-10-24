"""
WSGI config for thierry project.
It exposes the WSGI callable as a module-level variable named ``application``.
"""
# built in
import os

# third party
from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "thierry.settings")
application = get_wsgi_application()
