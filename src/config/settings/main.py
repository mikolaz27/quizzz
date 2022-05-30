from config.settings.base import *  # noqa:

DEBUG = False

ALLOWED_HOSTS = [
    "localhost",
]

CURRENT_ENV = "MAIN"
print(CURRENT_ENV)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["POSTGRES_DB"],  # noqa:
        "USER": os.environ["POSTGRES_USER"],  # noqa:
        "PASSWORD": os.environ["POSTGRES_PASSWORD"],  # noqa:
        "HOST": os.environ["POSTGRES_HOST"],  # noqa:
        "PORT": os.environ["POSTGRES_PORT"],  # noqa:
    },
}
