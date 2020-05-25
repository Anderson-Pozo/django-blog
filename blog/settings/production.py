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
        'NAME': 'dagb4ji1t9t16d',
        'USER': 'hhsotppmqzzbdu',
        'PASSWORD': '4e8554222f3beda5769559ec4dcf778dea592ad468c7c832ffd0442e4bc014e6',
        'HOST': 'ec2-50-17-90-177.compute-1.amazonaws.com',
        'PORT': '5432'
    }
}

STATICFILES_DIRS = (BASE_DIR, 'static')
