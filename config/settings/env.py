from .base import *

SECRET_KEY = 'django-insecure-gh&i5z2r#-s!$t1z)=rm00t5ci90*vdm0f4-z8w3d1b7)dcguv'

DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
