# Python Imports
import os

# Django imports
from django.conf import settings

DEFAULT_FILE_STORAGE = getattr( settings, "DEFAULT_FILE_STORAGE", settings.MEDIA_ROOT )
FILES_DIR_NAME = os.path.basename( DEFAULT_FILE_STORAGE )