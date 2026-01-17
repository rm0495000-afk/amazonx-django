"""
Django settings for ecom project.
Compatible with django-unfold + Render deployment
"""

from pathlib import Path

# --------------------------------------------------
# BASE
# --------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent


# --------------------------------------------------
# SECURITY
# --------------------------------------------------
SECRET_KEY = 'django-insecure-9wixmm73*kzpfbn%5d!ky!k7+$4mazbhlk4d)^w@@1#g6ot(=t'
DEBUG = True   # Render-la ippo True (login create panna)

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    ".onrender.com",
]


# --------------------------------------------------
# APPLICATIONS
# --------------------------------------------------
INSTALLED_APPS = [
    "jazzmin",               # 🔥 MUST BE FIRST
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "amazon.apps.AmazonConfig",
]

# --------------------------------------------------
# JAZZMIN ADMIN THEME CONFIG
# --------------------------------------------------
JAZZMIN_SETTINGS = {
    "site_title": "AmazonX Admin",
    "site_header": "AmazonX Dashboard",
    "site_brand": "AmazonX",
    "welcome_sign": "Welcome to AmazonX Admin",
    "copyright": "AmazonX",
    "topmenu_links": [
        {"name": "Home", "url": "/", "new_window": True},
        {"name": "View Site", "url": "/", "new_window": True},
    ],
    "show_sidebar": True,
    "navigation_expanded": True,
}




# --------------------------------------------------
# MIDDLEWARE
# --------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# --------------------------------------------------
# URLS
# --------------------------------------------------
ROOT_URLCONF = "ecom.urls"


# --------------------------------------------------
# TEMPLATES
# --------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "amazon" / "templates"],
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


# --------------------------------------------------
# WSGI
# --------------------------------------------------
WSGI_APPLICATION = "ecom.wsgi.application"


# --------------------------------------------------
# DATABASE
# --------------------------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# --------------------------------------------------
# PASSWORD VALIDATION
# --------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# --------------------------------------------------
# INTERNATIONALIZATION
# --------------------------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# --------------------------------------------------
# STATIC FILES
# --------------------------------------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_DIRS = [
    BASE_DIR / "amazon" / "static",
]


# --------------------------------------------------
# MEDIA FILES
# --------------------------------------------------
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


# --------------------------------------------------
# DEFAULT PRIMARY KEY
# --------------------------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# --------------------------------------------------
# DJANGO-UNFOLD CONFIG
# --------------------------------------------------
UNFOLD = {
    "SITE_TITLE": "AmazonX Admin",
    "SITE_HEADER": "AmazonX Dashboard",
    "SITE_URL": "/",
    "SHOW_VIEW_ON_SITE": True,

    "STYLES": [
        "/static/admin_fix.css",
    ],

    "COLORS": {
        "primary": {
            "500": "99 102 241",
            "600": "79 70 229",
            "700": "67 56 202",
        }
    },
}


# --------------------------------------------------
# 🔥 TEMP AUTO ADMIN (RENDER LOGIN FIX)
# --------------------------------------------------
# ⚠️ REMOVE THIS BLOCK AFTER LOGIN SUCCESS
if DEBUG:
    try:
        from django.contrib.auth.models import User
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(
                username="admin",
                email="admin@example.com",
                password="admin123"
            )
    except Exception:
        pass
