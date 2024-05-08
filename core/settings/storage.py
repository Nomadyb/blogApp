import os
from pathlib import Path
import environ


env = environ.Env()
environ.Env.read_env()

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# STATIC_URL = '/static/'
# Django Static Files Directory
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
