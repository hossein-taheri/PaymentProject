from mongoengine import *
import datetime


class Notification(Document):
    media = StringField(required=True)
    receivers = ListField(StringField())
    message = StringField()
    status_code = IntField(required=True, default=-1)
    created_at = DateTimeField(required=True, default=datetime.datetime.now)
