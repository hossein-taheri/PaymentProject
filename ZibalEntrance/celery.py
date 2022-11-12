import os

from celery import Celery

app = Celery('ZibalEntrance')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ZibalEntrance.settings')

app.config_from_object('django.conf:settings', namespace='CELERY')
