from pathlib import Path
import os

# BASE_DIR'ı storage.py dosyasında tanımla
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
# Django Static Files Directory
# STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
