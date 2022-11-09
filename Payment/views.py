from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


@require_http_methods(["POST"])
@csrf_exempt
def pay_factor(request, factor_id):
    print(factor_id)
    return HttpResponse("pay_factor test")


@require_http_methods(["POST"])
@csrf_exempt
def verify_payment(request, payment_id):
    print(payment_id)
    return HttpResponse("verify_payment test")
