# Python Imports
import os

# Django imports
from django.conf import settings

FILE_STORAGE = getattr( settings, "FILE_STORAGE", settings.MEDIA_ROOT )
FILES_DIR_NAME = os.path.basename( FILE_STORAGE )