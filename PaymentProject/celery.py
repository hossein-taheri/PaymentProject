import os

from celery import Celery

app = Celery('PaymentProject')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PaymentProject.settings')

app.config_from_object('django.conf:settings', namespace='CELERY')
