from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods
import os
import zibal.zibal as zibal
from Payment.mongo_models import Factor, Payment
from PaymentProject.tasks import send_sms

merchant = os.getenv("ZIBAL_MERCHANT")


@require_http_methods(["GET"])
def pay_factor(request, factor_id):
    factor = Factor.objects.get(
        pk=factor_id
    )

    payment = Payment(
        factor_id=factor.id,
        amount=factor.amount,
    ).save()

    callback_url = f"http://{request.get_host()}/payment/verify_payment/{payment.id}"

    zb = zibal.zibal(merchant, callback_url)
    amount = payment.amount * 10
    request_to_zibal = zb.request(amount)

    if request_to_zibal['result'] != 100:
        return HttpResponse(status=500)

    payment.trace_id = str(request_to_zibal['trackId'])
    payment.save()

    return redirect(f"https://gateway.zibal.ir/start/{payment.trace_id}")


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

        send_sms.delay(factor.phone_number, f"Your factor with {factor.amount * 10} IRR paid")

    return HttpResponse(payment.status)
