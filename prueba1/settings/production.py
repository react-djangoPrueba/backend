from .settings import *
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-zj1$87yai!pwf9!u5oehzsh)a$(5ws&8tji0tp8%79x=1h6xc6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


ALLOWED_HOSTS = ['backend-authql.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'df29mffieflj4e',
        'USER': 'lasaoiuqdxpdpv',
        'PASSWORD':'cb9320b0ebaef0f48acce5c007ceeef12235140f0807d0674434a460dbfa0394',
        'HOST':'ec2-23-23-199-57.compute-1.amazonaws.com',
        'PORT':5432
    }
}
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'deliveryfoodpopayan@gmail.com'
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_USER')
EMAIL_USE_TLS = True
EMAIL_PORT = 587
