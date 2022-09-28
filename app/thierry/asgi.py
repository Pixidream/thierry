"""
ASGI config for thierry project.

It exposes the ASGI callable as a module-level variable named ``application``.
"""
# built in
import os

# third party
from django.core.asgi import get_asgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "thierry.settings")
application = get_asgi_application()
