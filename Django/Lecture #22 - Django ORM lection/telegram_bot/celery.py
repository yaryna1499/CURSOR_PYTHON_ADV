from celery import Celery
import os
from celery.schedules import schedule

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cursor.settings")
app = Celery("telegram_bot")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.worker_pool = "gevent"
app.autodiscover_tasks()
