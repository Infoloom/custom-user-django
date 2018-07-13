from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*']
STATIC_ROOT = os.path.join(BASE_DIR, 'base_static')
STATIC_URL = '/static/'
STATICFILES_DIR = 'base_static'
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = ['http://localhost:3000']