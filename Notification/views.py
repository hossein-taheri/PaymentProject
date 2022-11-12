import os

from django.shortcuts import render
from kavenegar import *

user_name = os.getenv('RAYGANSMS_USERNAME')
password = os.getenv('RAYGANSMS_PASSWORD')
sender_number = os.getenv('RAYGANSMS_SENDER_NUMBER')


def SendSMS(receiver, message):
    import requests

    url = "https://RayganSMS.com/SendMessageWithUrl.ashx"

    params = {
        "UserName": user_name,
        "Password": password,
        "PhoneNumber": sender_number,
        "MessageBody": message,
        "RecNumber": receiver,
    }

    response = requests.request("GET", url, params=params)

    print(response.text)
