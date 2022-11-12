import os

from celery import Celery

app = Celery('ZibalEntrance')

app.config_from_object('ZibalEntrance.celery_config')

