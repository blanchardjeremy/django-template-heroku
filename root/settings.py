import sys
import os
# assume we are ./apps/mainsite/settings.py
from urlparse import urlparse, uses_netloc
uses_netloc.append('postgres')

APPS_DIR = os.path.dirname(__file__)
if APPS_DIR not in sys.path:
    sys.path.insert(0, APPS_DIR)
from mainsite import TOP_DIR


def boolcheck(s):
    if isinstance(s, basestring):
        return s.lower() in ("yes", "true", "t", "1")
    else:
        return bool(s)

DEBUG = boolcheck(os.environ.get('DEBUG', 'False'))
TEMPLATE_DEBUG = DEBUG

# Whether or not django should serve static files through its wsgi server. Suggested against in the docs, but makes deployment to heroku easier.
DJANGO_SERVE_STATIC = boolcheck(os.environ.get('DJANGO_SERVE_STATIC', 'True'))


INSTALLED_APPS = [
    'mainsite',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
]

JINGO_EXCLUDE_APPS = ['admin', 'registration',]



MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

TEMPLATE_CONTEXT_PROCESSORS = [
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
]

TEMPLATE_LOADERS = [
	'jingo.Loader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
]


TEMPLATE_DIRS = [
    os.path.join(TOP_DIR, 'templates'),
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]


STATICFILES_DIRS = [
]


MEDIA_ROOT =  os.environ.get('MEDIA_ROOT', os.path.join(TOP_DIR, 'uploads'))
STATIC_ROOT = os.environ.get('STATIC_ROOT', os.path.join(TOP_DIR, 'static'))
MEDIA_URL = os.environ.get('MEDIA_URL', '/uploads/')
STATIC_URL = os.environ.get('STATIC_URL', '/static/')
ADMIN_MEDIA_PREFIX = STATIC_URL+'admin/'

ROOT_URLCONF = 'mainsite.urls'


SECRET_KEY = ''
TIME_ZONE = 'America/Los_Angeles'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


url = urlparse(os.environ['DATABASE_URL'])
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': url.path[1:],
        'USER': url.username,
        'PASSWORD': url.password,
        'HOST': url.hostname,
        'PORT': url.port,
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': '',
        'TIMEOUT': 300,
        'KEY_PREFIX': '',
        'VERSION': 1,
    }
}


if DEBUG:
    MIDDLEWARE_CLASSES.insert(0,'debug_toolbar.middleware.DebugToolbarMiddleware')
    INSTALLED_APPS.append('debug_toolbar')
    INTERNAL_IPS = (
       '127.0.0.1',
    )
    JINGO_EXCLUDE_APPS.append('debug_toolbar')
    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False
    }

