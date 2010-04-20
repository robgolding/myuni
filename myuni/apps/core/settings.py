from django.conf import settings

STATIC_URL = getattr(settings, 'STATIC_URL', '')
