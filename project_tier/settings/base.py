"""
Django settings for project_tier project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)


# Configuration from environment variables
env = os.environ.copy()


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/
ADMINS = []


# Application definition

INSTALLED_APPS = (
    'project_tier.core',
    'project_tier.events',
    'project_tier.home',
    'project_tier.news',
    'project_tier.people',  # Use the `network` app instead.
    'project_tier.standard',
    'project_tier.testimonials',
    'project_tier.search',
    'project_tier.exercises',
    'project_tier.course_materials',
    'project_tier.network',
    'project_tier.specs',

    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',

    'modelcluster',
    'compressor',
    'taggit',
    'django_nose',
    'storages',
    'wagtailfontawesome',
    'wagtailemoji',
    'wagalytics',
    'wagtaillinkchecker',
    'draftailmodal',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'wagtail.contrib.modeladmin',
)

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
)

ROOT_URLCONF = 'project_tier.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'project_tier.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.config(conn_max_age=600)
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'project_tier',
        }
    }


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-US'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--cover-package=project_tier',
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# Django compressor settings
# http://django-compressor.readthedocs.org/en/latest/settings/

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)


# Celery settings
# When you have multiple sites using the same Redis server,
# specify a different Redis DB. e.g. redis://localhost/5

BROKER_URL = 'redis://'

CELERY_SEND_TASK_ERROR_EMAILS = True
CELERYD_LOG_COLOR = False


# Wagtail settings

WAGTAIL_SITE_NAME = "project_tier"


# Taggit
# https://django-taggit.readthedocs.io/en/latest/

# Just query tags in a case-insensitive way instead.
# https://github.com/alex/django-taggit/issues/448
TAGGIT_CASE_INSENSITIVE = False


# Analytics

if 'ANALYTICS_ENABLED' in env:
    ANALYTICS_ENABLED = env['ANALYTICS_ENABLED'].lower() in ['1', 'true']

if 'GA_KEY_CONTENT' in env and 'GA_VIEW_ID' in env:
    GA_KEY_CONTENT = env['GA_KEY_CONTENT']
    GA_VIEW_ID = env['GA_VIEW_ID']


# Link checker

DEFAULT_PER_PAGE = 50
