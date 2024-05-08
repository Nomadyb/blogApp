from pathlib import Path
import os
import environ
from datetime import timedelta


env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.

"""
BASE_DIR  dosya yolunun başlangıç noktasını belirtir.
bu sebeple ilk olarak settings.py dosyasının bulunduğu dizini alır.
sonra bir üst dizine çıkarak projenin ana dizinine ulaşır.
normal bir yapılandırmada iki parent yeterli ama bu yapılandırmada settings.py dosyası settings klasörü altında olduğu için üç parent kullanıldı.
"""
BASE_DIR = Path(__file__).resolve().parent.parent.parent
# BASE_DIR = Path(__file__).resolve().parent.parent


# SECRET_KEY = os.getenv("SECRET_KEY")
SECRET_KEY = 'django-insecure-^!kynt^88*zw-i9949x&n^i9!gi)g+9gkzj0hxh+lvm4tg$j*i'

# TODO:canlıya alırken False yapılacak unutma

DEBUG = os.environ.get('DEBUG', default=False)
ALLOWED_HOSTS = ['*']

# ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", default="*")

AUTH_USER_MODEL = "users.User"



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'dj_rest_auth',
    'dj_rest_auth.registration',

    'users',
    'blogger',
    'administration',

    'django_crontab',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# PostgreSQL configuration bu konfigrasyon railway üzerinde çalışacak şekilde ayarlandı.
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': "railway",  # Change to 'blogApp'
#         'USER': "postgres",
#         'PASSWORD': "toMjGSWmwsRncoRLtAnyLuMCeYzdvvmJ",
#         'HOST': "roundhouse.proxy.rlwy.net",
#         'PORT': "35425"
#     }
# }





# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.getenv("SQL_DATABASE", "blogApp"),  # Change to 'blogApp'
#         'USER': os.getenv("SQL_USER", "postgres"),
#         'PASSWORD': os.getenv("SQL_PASSWORD", "postgrespassword"),
#         'HOST': os.getenv("SQL_HOST", "127.0.0.1"),
#         'PORT': os.getenv("SQL_PORT", "5432"),
#     }
# }






DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Simple JWT Settings
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=360),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=3),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
}

# CORS Settings
CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:8000',
    'http://127.0.0.1:3000',
]
CORS_ALLOW_ALL_ORIGINS = True

# Rest Auth Settings
REST_AUTH = {
    "USE_JWT": True,
    "JWT_AUTH_HTTPONLY": False
}

# Authentication Backend Settings
AUTHENTICATION_BACKENDS = [
    "users.backends.EmailAuthBackend",
    "django.contrib.auth.backends.ModelBackend",
]

STATIC_ROOT = BASE_DIR / 'staticfiles'


# Media Settings
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Crontab Settings
CRONJOBS = [
    ('*/1 * * * *', '/usr/local/bin/python /usr/src/BlogProject/blog-cron.py >> /var/log/cron.log 2>&1'),
]
