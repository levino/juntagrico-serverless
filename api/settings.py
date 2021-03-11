import os

DEBUG = os.environ.get('DEBUG')

ALLOWED_HOSTS = [os.environ.get('VERCEL_URL')]

SECRET_KEY = os.environ.get('SECRET_KEY')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

IMPERSONATE = {
    'REDIRECT_URL': '/my/profile',
}

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'impersonate',
    'juntagrico',
    'crispy_forms',
]

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DATABASE_BACKEND', 'django.db.backends.sqlite3'),
        'NAME':  os.environ.get('DATABASE_NAME', 'juntagrico.sqlite3'),
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'PORT': os.environ.get('DATABASE_PORT'),
    }
}

ROOT_URLCONF = 'api.urls'

AUTHENTICATION_BACKENDS = (
    'juntagrico.util.auth.AuthenticateWithEmail',
    'django.contrib.auth.backends.ModelBackend'
)

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'impersonate.middleware.ImpersonateMiddleware',
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = os.environ.get('EMAIL_HOST_PORT')
EMAIL_USE_TLS = True

WHITELIST_EMAILS = os.environ.get('WHITELIST_EMAILS', '').split(',')

def whitelist_email_from_env(var_env_name):
    email = os.environ.get(var_env_name)
    if email:
        WHITELIST_EMAILS.append(email)

if DEBUG is True:
    for key in os.environ.keys():
        if key.startswith("EMAIL_WHITELISTED"):
            whitelist_email_from_env(key)

STATIC_ROOT = os.path.join(BASE_DIR, '../public/static')
STATIC_URL = '/static/'

LANGUAGE_CODE = 'de-DE'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

DATE_INPUT_FORMATS = ['%d.%m.%Y', ]

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader'
            ],
            'debug': True
        },
    },
]

LOGIN_REDIRECT_URL = "/my/home"

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'juntagrico/locale'),
)

CRISPY_TEMPLATE_PACK = 'bootstrap4'
CRISPY_FAIL_SILENTLY = not DEBUG

ORGANISATION_NAME = 'SpeiseGut'
SERVER_URL = 'speisegut.com'

ADMINPORTAL_NAME = 'SpeiseGut'

INFO_EMAIL = 'juntagrico@speisegut.com'