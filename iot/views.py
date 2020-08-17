from django.http import JsonResponse, HttpResponseBadRequest
from meters.models import Meter
from django.core.exceptions import ValidationError

def update_user_info(request):
    ''' 
    This will return a user's information
    Example:
    http://127.0.0.1:8000/api/iot?meter-id=8026&token=434300772164515017&usage=140
    '''

    meter_id    = int(request.GET.get('meter-id', ''))
    token       = int(request.GET.get('token', ''))
    usage       = int(request.GET.get('usage', ''))

    # Check if the user is authentic
    try:
        if (meter := Meter.objects.get(meter_id=meter_id)):
            if meter and meter.meter_token == token:
                # Do the business process
                meter.balance = int(usage)
                meter.save_iot()
                return JsonResponse({
                    "balance": meter.customer_balance
                }, status=200)
        else:
            JsonResponse({
                'message' : "Invalid authentication details"
            }, status=401)
    except (ValidationError, ValueError) as e:
        message = e.message
        if not e:
            message = "Could not handle request"
        return JsonResponse({
            "message" : message
        }, status=400)