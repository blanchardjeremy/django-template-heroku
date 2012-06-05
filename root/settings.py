import os
from urlparse import urlparse, uses_netloc

from mainsite import TOP_DIR


##
#
#  Debug Flags
#
##

def boolcheck(s):
    if isinstance(s, basestring):
        return s.lower() in ("true", "yes", "t", "1")
    else:
        return bool(s)

DEBUG = boolcheck(os.environ.get('DEBUG', False))
TEMPLATE_DEBUG = DEBUG
DEBUG_TOOLBAR = boolcheck(os.environ.get('DEBUG_TOOLBAR', DEBUG))

# Whether or not django should serve static files through its wsgi server. Suggested against in the docs, but makes deployment to heroku easier.
DJANGO_SERVE_STATIC = boolcheck(os.environ.get('DJANGO_SERVE_STATIC', DEBUG))


##
#
#  Important Stuff
#
##

INSTALLED_APPS = [
	# This site
    'mainsite',

	# Dependencies
    'bootstrap',
    'gunicorn',

	# Django
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    # More dependencies (that need to be lower in the list)
    #'south',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Secret key should be the same on all of your servers. You can put it directly into settings if that is safe for you. Or you can specify it as an environment variable.
# Get one here: http://www.miniwebtool.com/django-secret-key-generator/
SECRET_KEY = os.environ.get('SECRET_KEY', 'PUT_A_SECRET_KEY_HERE')



##
#
#  Templates
#
##

TEMPLATE_LOADERS = [
	'jingo.Loader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
]

TEMPLATE_DIRS = [
    os.path.join(TOP_DIR, 'templates'),
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

JINGO_EXCLUDE_APPS = ['admin', 'registration',]


##
#
#  Static Files
#
##

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATIC_ROOT = os.environ.get('STATIC_ROOT', os.path.join(TOP_DIR, 'staticfiles'))
STATIC_URL = os.environ.get('STATIC_URL', '/static/')
STATICFILES_DIRS = [
]


##
#
#  Media Files
#
##

MEDIA_ROOT =  os.environ.get('MEDIA_ROOT', os.path.join(TOP_DIR, 'mediafiles'))
MEDIA_URL = os.environ.get('MEDIA_URL', '/media/')


##
#
#  Database
#
##

uses_netloc.append('postgres')
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


##
#
#  Caching
#
##

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': '',
        'TIMEOUT': 300,
        'KEY_PREFIX': '',
        'VERSION': 1,
    }
}


##
#
#  Logging
#
##

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


##
#
#  Misc.
#
##

SITE_ID = 1

ROOT_URLCONF = 'mainsite.urls'

USE_I18N = False
USE_L10N = False
USE_TZ = True

TIME_ZONE = 'America/Los_Angeles'
LANGUAGE_CODE = 'en-us'



##
#
#  Debug Toolbar
#
##

def debug_toolbar_available():
    try:
        import debug_toolbar
        return True
    except ImportError:
        return False

if DEBUG_TOOLBAR and debug_toolbar_available():
    MIDDLEWARE_CLASSES.insert(0,'debug_toolbar.middleware.DebugToolbarMiddleware')
    INSTALLED_APPS.append('debug_toolbar')
    INTERNAL_IPS = (
       '127.0.0.1',
    )
    JINGO_EXCLUDE_APPS.append('debug_toolbar')
    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False
    }

