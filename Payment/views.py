from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import os
import zibal.zibal as zibal
from Payment.mongo_models import Factor, Payment

merchant = os.getenv("ZIBAL_MERCHANT")


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

    callback_url = f"http://127.0.0.1:8000/payment/verify_payment/{payment.id}"

    zb = zibal.zibal(merchant, callback_url)
    amount = payment.amount * 10
    request_to_zibal = zb.request(amount)

    if request_to_zibal['result'] != 100:
        return HttpResponse(status=500)

    payment.trace_id = str(request_to_zibal['trackId'])
    payment.save()

    return redirect(f"https://gateway.zibal.ir/start/{payment.trace_id}")


@csrf_exempt
@require_http_methods(["GET"])
def verify_payment(request, payment_id):
    payment = Payment.objects.get(
        pk=payment_id
    )

    zb = zibal.zibal(merchant, None)

    verify_zibal = zb.verify(payment.trace_id)
    status = verify_zibal['result']

    payment.status = verify_zibal['message']
    payment.status_code = verify_zibal['result']
    payment.save()

    if status == 100 or status == 201:  # payment was successful and now factor's status must change to paid
        factor = Factor.objects.get(
            pk=payment.factor_id.id
        )
        factor.status = "paid"
        factor.status_code = 1
        factor.save()

        # send message was successful to celery

    return HttpResponse(payment.status)
