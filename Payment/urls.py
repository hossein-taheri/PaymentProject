from django.contrib import admin
from django.urls import path

from Payment import views

urlpatterns = [
    path('pay_factor/<str:factor_id>', views.pay_factor, name="payment.pay_factor"),
    path('verify_payment/<str:payment_id>', views.verify_payment, name="payment.verify_payment"),
]
