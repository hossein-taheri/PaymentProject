import os
import requests
from Notification.mongo_models import Notification

user_name = os.getenv('RAYGANSMS_USERNAME')
password = os.getenv('RAYGANSMS_PASSWORD')
sender_number = os.getenv('RAYGANSMS_SENDER_NUMBER')


def SendSMS(receiver, message):
    url = "https://RayganSMS.com/SendMessageWithUrl.ashx"

    params = {
        "UserName": user_name,
        "Password": password,
        "PhoneNumber": sender_number,
        "MessageBody": message,
        "RecNumber": receiver,
    }

    response = requests.request("GET", url, params=params)

    Notification(
        media="SMS",
        receivers=[receiver],
        message=message,
        status_code=response.status_code
    ).save()
