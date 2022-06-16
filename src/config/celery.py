from celery import Celery

app = Celery("quizzz")
app.config_from_object(
    "django.conf.settings",
    namespace="CELERY"
)
app.autodiscover_tasks()
