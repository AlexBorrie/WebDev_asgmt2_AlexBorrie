"""
WSGI config for AlexBorrie_asgmt2_ISCG7420 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AlexBorrie_asgmt2_ISCG7420.settings')

application = get_wsgi_application()
