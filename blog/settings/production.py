from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['apdjangoblog.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db here',
        'USER': 'user here',
        'PASSWORD': 'password here',
        'HOST': 'host here',
        'PORT': '5432'
    }
}

STATICFILES_DIRS = (BASE_DIR, 'static')
