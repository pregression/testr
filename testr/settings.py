"""
Django settings for testr project.

Generated by 'django-admin startproject' using Django 2.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
from django.conf import settings
from dj_database_url import parse as db_url
from decouple import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='secret')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = [
    'localhost',
    '.herokuapp.com',
    '.pregression.com',
]

# Application definition
APP_NAME = 'Pregression'
WAGTAIL_SITE_NAME = APP_NAME
APP_TITLE_DELIMITER = '|'
ESTABLISHED_YEAR = 2018
SITE_ID = 2
SOCIALACCOUNT_QUERY_EMAIL = True
TELLME_FEEDBACK_EMAIL = 'incoming+pregression/testr@incoming.gitlab.com'
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.bitbucket_oauth2',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.gitlab',
    'allauth.socialaccount.providers.google',

    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.contrib.search_promotions',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',

    'testr.blog.apps.BlogConfig',
    'testr.core.apps.CoreConfig',
    'testr.custom_auth.apps.CustomAuthConfig',
    'testr.marketing.apps.MarketingConfig',
    'testr.projects.apps.ProjectsConfig',

    'anymail',
    'tellme',
    'modelcluster',
    'taggit',
    'robots',
    'compressor',
    'behave_django',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
    'testr.core.middleware.AuthRequiredMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]

ROOT_URLCONF = 'testr.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'testr.core.context_processors.current_year',
                'testr.core.context_processors.established_year',
                'testr.core.context_processors.formatted_copyright_year',
                'testr.core.context_processors.app_name',
                'testr.core.context_processors.title_delimiter',
            ],
        },
    },
]

WSGI_APPLICATION = 'testr.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': config(
        'DATABASE_URL',
        default='postgres://testr:testr@localhost:5432/testr',
        cast=db_url,
    ),
}

# Caching setup
if not DEBUG:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': config('MEMCACHE_SERVERS', default="localhost:11211"),
        },
    }
else:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    }

## Custom User Model
#
AUTH_USER_MODEL = 'custom_auth.User'

AUTHENTICATION_BACKENDS = (
    # Needed for local auth
    'django.contrib.auth.backends.ModelBackend',
    # Backends to support all sorts of authentication methods from allauth
    'allauth.account.auth_backends.AuthenticationBackend',
)

ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_PASSWORD_MIN_LENGTH = 6
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "optional"
ACCOUNT_LOGIN_ATTEMPTS = 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_USERNAME_BLACKLIST = []
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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

# Password hashers
# https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-PASSWORD_HASHERS
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
]

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
]

# Override login redirect
LOGIN_REDIRECT_URL = '/projects'

# Whitelist routes that don't require login
WHITELIST_ROUTES = [
    settings.LOGIN_URL,
    STATIC_URL,
    MEDIA_URL,
    '/admin/',
    '/admin/login/',
    '/accounts/password_reset/',
    '/accounts/signup/',
    '/accounts/google/login/',
    '/terms/',
    '/privacy/',
    '/license/',
    r'/blog/*',
    r'/tags/*',
]

# Compressor setup
COMPRESS_OFFLINE = config('COMPRESS_ASSETS', default=False, cast=bool)

COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.rCSSMinFilter',
]

COMPRESS_JS_FILTERS = [
    'compressor.filters.jsmin.SlimItFilter',
]

COMPRESS_STORAGE = 'compressor.storage.GzipCompressorFileStorage'

DEFAULT_FROM_EMAIL = "support@pregression.com"
EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"
ANYMAIL = {
    'MAILGUN_API_KEY': os.getenv('MAILGUN_API_KEY'),
    'MAILGUN_SENDER_DOMAIN': os.getenv('MAILGUN_DOMAIN'),
}
