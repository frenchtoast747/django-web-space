from django.conf import settings

FILES_DIR = getattr( settings, "FILES_DIR", settings.MEDIA_ROOT )