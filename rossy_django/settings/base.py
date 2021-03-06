"""
Django settings for rossy_django project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6-9u20(^1j7$tke_q1rw0=-3*sw0l#o10k(g)9p1kpdq6afzkl'


# Application definition

INSTALLED_APPS = [
    'suit',
    'aplicacion.registration',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # aplicaciones propias
    'aplicacion.usuarios',
    'aplicacion.clientes',
    'aplicacion.geolocalizacion',
    'aplicacion.bodega',
    'aplicacion.facturacion',
    'aplicacion.rutas',
    'aplicacion.utilidades',
    'aplicacion.website',

    # aplicaciones de terceros
    'easy_select2',
    'import_export',
    'easy_pdf',
    'django_extensions',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Captura el request actual y el usuario en el almacenamiento local de subprocesos.
    'crum.CurrentRequestUserMiddleware',
]

ROOT_URLCONF = 'rossy_django.urls'

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

SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'Rossy',
    'HEADER_DATE_FORMAT': 'l, j. F Y ',
    'HEADER_TIME_FORMAT': 'h: i a',

    # formularios
    # 'SHOW_REQUIRED_ASTERISK': verdadero, # predeterminado verdadero
    # 'CONFIRM_UNSAVED_CHANGES': verdadero, # predeterminado verdadero

    # menu
    'SEARCH_URL': '',
    # 'MENU_ICONS': {
    #     'clientes': 'icon-briefcase',
    #     'bodega': 'icon-th-large',
    #     'facturacion': 'icon-list',
    #     'rutas': 'icon-road',
    #     'geolocalizacion': 'icon-map-marker',
    #     'usuarios': 'icon-user',
    #     'auth': 'icon-lock',
    #     'admin': 'icon-cog',
    # },
    'MENU_OPEN_FIRST_CHILD': False, # Predeterminado True
    #' MENU_EXCLUDE ': (' auth.group ',),
    'MENU': (
        {'label': 'Dashboard', 'icon': 'icon-list-alt', 'url': '/dashboard/'},
        {'app': 'clientes', 'icon': 'icon-briefcase', 'models': ('Cliente',)},
        {'app': 'bodega', 'icon': 'icon-th-large', 'models': ('ProduccionProducto', 'ProductoDetallado', 'Producto',
                                                              'CompraInsumo', 'InsumoDetallado', 'Insumo',
                                                              'Marca', 'UnidadMedida',)},
        {'app': 'facturacion', 'icon': 'icon-list', 'models': ('Factura', 'ProductoVenta', 'FacturaCredito', 'AbonoCredito',)},
        {'app': 'rutas', 'icon': 'icon-road', 'models': ('Ruta', 'Zona',)},
        {'app': 'geolocalizacion', 'icon': 'icon-map-marker', 'models': ('Pais', 'Departamento', 'Ciudad', 'Barrio')},
        {'app': 'usuarios', 'icon': 'icon-user', 'models': ('Usuario',)},
        {'app': 'auth', 'icon': 'icon-lock', 'models': ('group',)},
        {'app': 'admin', 'icon': 'icon-cog', 'models': ('logentry',)},
    ),

    # misc
    # 'LIST_PER_PAGE': 15
}

WSGI_APPLICATION = 'rossy_django.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# START CRISPY FORMS CONFIGURATION
CRISPY_TEMPLATE_PACK = 'bootstrap3'
# END CRISPY FORMS CONFIGURATION

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
STATIC_URL = '/static/'


# Media config
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


AUTH_USER_MODEL = "usuarios.Usuario"

LOGIN_REDIRECT_URL = 'index'
LOGOUT_REDIRECT_URL = 'index'