from ._base import *  # noqa

TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'channels'
    }
}

INSTALLED_APPS = INSTALLED_APPS + (
    'debug_toolbar', 'django_extensions'
)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SITE_ID = 1
