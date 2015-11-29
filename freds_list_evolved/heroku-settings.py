from .settings import *

DEBUG = True
SECRET_KEY = os.environ['SECRET_KEY']

BLACKLIST = ['debug_toolbar', 'django_extensions']
INSTALLED_APPS = tuple([app for app in INSTALLED_APPS if app not in BLACKLIST])

import dj_database_url
DATABASES['default'] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIR = (
    os.path.join(BASE_DIR, 'static')
)

CACHES = {
    'default': {
        'BACKEND': 'django_bmemcached.memcached.BMemcached',
        'LOCATION': os.environ.get('MEMCACHEDCLOUD_SERVERS').split(','),
        'OPTIONS': {
                    'username': os.environ.get('memcached-app43966617'),
                    'password': os.environ.get('0KDfdOwTX05ptoou')
            }
    }
}