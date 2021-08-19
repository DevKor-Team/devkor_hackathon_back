from .base import *

DEBUG = False

ALLOWED_HOSTS = ["*"]  # no domain yet

CORS_ALLOW_ALL_ORIGINS = False
CORS_ORIGIN_WHITELIST = []

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": os.getenv("DB_NAME"),
#         "USER": os.getenv("DB_USERNAME"),
#         "PASSWORD": os.getenv("DB_PASSWORD"),
#         "HOST": os.getenv("DB_HOST"),
#         "PORT": "5432",
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


LOGIN_REDIRECT_URL = "/"

MIDDLEWARE = [*MIDDLEWARE, "django.middleware.csrf.CsrfViewMiddleware"]
