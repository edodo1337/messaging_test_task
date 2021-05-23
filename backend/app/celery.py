from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')

celery_app = Celery('app', backend='redis', broker=f'redis://{REDIS_HOST}:6379/1')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
celery_app.now = timezone.now
