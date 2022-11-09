from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

import zibal.zibal as zibal
from Payment.mongo_models import Factor, Payment
import os


@csrf_exempt
@require_http_methods(["POST"])
def pay_factor(req, factor_id):
    factor = Factor.objects.get(
        pk=factor_id
    )

    payment = Payment(
        factor_id=factor.id,
        amount=factor.amount,
    ).save()

    merchant = os.getenv("ZIBAL_MERCHANT")
    callback_url = f"http://127.0.0.1:8000/payment/verify_payment/{payment.id}"

    zb = zibal.zibal(merchant, callback_url)
    amount = payment.amount * 10
    request_to_zibal = zb.request(amount)

    if request_to_zibal['result'] is not 100:
        return HttpResponse(status=500)

    payment.trace_id = str(request_to_zibal['trackId'])
    payment.save()

    return redirect(f"https://gateway.zibal.ir/start/{payment.trace_id}")


@csrf_exempt
@require_http_methods(["POST"])
def verify_payment(request, payment_id):
    print(payment_id)
    return HttpResponse("verify_payment test")
