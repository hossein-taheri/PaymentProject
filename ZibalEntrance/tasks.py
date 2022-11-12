import os

from Notification.views import send_notification_via_sms
from .celery import app


@app.task(bind=True)
def send_sms(self, receiver, message):
    send_notification_via_sms(
        receiver,
        message
    )
