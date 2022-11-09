from mongoengine import *
import datetime


class Factor(Document):
    order_id = ObjectIdField(required=True, unique=True)
    amount = IntField(required=True)
    status = StringField(max_length=10, required=True, default="created")  # created - paid
    status_code = IntField(required=True, default=-1)
    created_at = DateTimeField(required=True, default=datetime.datetime.now)


class Payment(Document):
    amount = IntField(required=True)
    factor_id = ReferenceField(Factor)
    trace_id = StringField(max_length=50, required=False)
    status = StringField(max_length=10, required=True, default="not-paid")  # not-paid , succeeded , failed
    status_code = IntField(required=True, default=-1)  # default = -1
    status_description = StringField(required=False)
    created_at = DateTimeField(required=True, default=datetime.datetime.now)
