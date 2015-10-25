# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
import dotenv
import logging
logger = logging.getLogger(__name__)


from os.path import expanduser
home = expanduser("~")
dotenv.read_dotenv(os.path.join('.','.env'))

DEPLOYMENT = os.environ.get('DEPLOYMENT','production')
SITE_URL = os.environ.get('SITE_URL','https://localhost')
BASE_DIR = os.environ.get('BASE_DIR',os.path.dirname(os.path.realpath(__file__)))
APPLICATION_TITLE = os.environ.get('APPLICATION_TITLE',"Bitposter PoC")
BRAND = ''

DB_NAME = os.environ.get('DB_NAME','mysite')
DB_USER = os.environ.get('DB_USER','db_user')
DB_PASS = os.environ.get('DB_PASS','ee0Er8Hbg9')
DEBUG = bool(os.environ.get('DEBUG', False))
DEBUG_VALUE = os.environ.get('DEBUG', False)

PATH_LOG = os.path.join(BASE_DIR,'log')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#QM\\D8lfx9CZLW5V!BAcm)l\\mKX95KuZ:r4!BRcL)Ir]5Tsq3y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

LOGIN_REDIRECT_URL = '/msg/home/'
LOGIN_URL = '/login/'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'msg',
)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', 
        'NAME': DB_NAME, 
        'USER': DB_USER,
        'PASSWORD': DB_PASS,
        'HOST': '',       
        'PORT': '', 
    },
}
# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-uk'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'Europe/London'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/var/prj/mysite/mysite/static'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
            },
        'logfile': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename':os.path.join(PATH_LOG,'mysite.log'),
            'maxBytes': 5000000,
            'backupCount': 2,
            'formatter': 'standard',
        },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'standard'
            },
    },
    'loggers': {
        'django': {
            'handlers':['console','logfile'],
            'propagate': True,
            'level':'ERROR',
        },
        'django.db.backends': {
            'handlers': ['logfile'],
            'level': 'ERROR',
            'propagate': False,
        },
        'mysite': {
            'handlers': ['logfile','console'],
            'level': 'DEBUG',
            },
        'doc': {
            'handlers': ['logfile','console'],
            'level': 'DEBUG',
            },
        '__main__': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}


# make sure we have our admin user and token
# TODO: for testing only: get rid of this
try:
    import django
    from django.contrib.auth.models import User
    from rest_framework.authtoken.models import Token
    from django.conf import settings
    django.setup()

    username = 'admin'
    password = 'admin'
    email = 'admin@example.com'
    if not User.objects.filter(username=username).exists():
        user = User.objects.create_superuser(username, email, password)
    user = User.objects.get(username=username)
    token, _ = Token.objects.get_or_create(user=user)
except Exception as e:
    print e
    
