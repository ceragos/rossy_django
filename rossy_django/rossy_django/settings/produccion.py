from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'willitapas$rossy',
        'USER': 'willitapas',
        'PASSWORD': 'Wlto8715',
        'HOST': 'willitapas.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}
