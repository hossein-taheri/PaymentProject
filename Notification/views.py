import os

from django.shortcuts import render
from kavenegar import *

kavenegar_api_key = os.getenv("KAVENEGAR_API_KEY")
print(kavenegar_api_key)


