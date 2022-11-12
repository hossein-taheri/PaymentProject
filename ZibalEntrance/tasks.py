import os

from .celery import app


@app.task(bind=True)
def send_sms(self, receiver, message):
    print(os.getenv('RAYGANSMS_USERNAME'))
    print("SMS Sended")
