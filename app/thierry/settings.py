"""
Django settings for thierry project.
"""
# built in
from pathlib import Path
from typing import List
from os import getenv

# -----------------------------------------
# ------------ DJANGO SETTINGS ------------
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = getenv("THIERRY_SECRET_KEY")

DEBUG = int(getenv("THIERRY_DEBUG", 0))

ALLOWED_HOSTS: List[str] = getenv("THIERRY_ALLOWED_HOSTS", "").split(";")

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "thierry.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "thierry.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": getenv("THIERRY_DB_NAME"),
        "USER": getenv("THIERRY_DB_USERNAME"),
        "PASSWORD": getenv("THIERRY_DB_PASSWORD"),
        "HOST": getenv("THIERRY_DB_HOST"),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = getenv("THIERRY_LANG_CODE", "fr-fr")

TIME_ZONE = getenv("THIERRY_TZ", "Europe/Paris")

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# -----------------------------------------
# ------------ CUSTOM SETTINGS ------------
