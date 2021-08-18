from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

client_encoding = "UTF8"
default_transaction_isolation = "read committed"

INTERNAL_IPS = ["127.0.0.1"]
LOGIN_REDIRECT_URL = "http://localhost:3000/"
