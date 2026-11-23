"""
ASGI config for learning_log project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

#had to update to learning_logs instead of learning_log was throughing an error
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_logs.settings")

application = get_asgi_application()
