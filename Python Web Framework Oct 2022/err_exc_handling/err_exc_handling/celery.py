import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "err_exc_handling.settings")
app = Celery("djangoProject")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
