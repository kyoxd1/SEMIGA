from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',
        'USER' : 'postgres',
        'PASSWORD' : 'C7x5g6GXa0uRd05BN23h',
        'HOST' : 'containers-us-west-61.railway.app',
        'PORT' : '5858',   
    }
}