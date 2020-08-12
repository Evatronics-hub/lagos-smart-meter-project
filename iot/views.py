from django.http import JsonResponse, HttpResponseBadRequest
from meters.models import Meter

def update_user_info(request):
    ''' 
    This will return a user's information
    Example:
    http://example.com/api/iot/&meter-id=1253292%token=138619a0n983n93i29x920&usage=140
    '''

    meter_id = request.GET.get('meter', '')
    token = request.GET.get('token', '')
    usage = request.GET.get('usage', '')

    # Check if the user is authentic
    try:
        if (user := Meter.objects.get(meter_id=meter_id)):
            if user and user.meter_token == token:
                # Do the business process
                user.customer_balance -= int(usage)
                user.save()
                return JsonResponse({
                    "balance": user.customer_balance
                }, status=200)
        else:
            JsonResponse({
                'message' : "Invalid authentication details"
            }, status=401)
    except ValueError:
        return JsonResponse({
            "message" : "Could not handle request"
        }, safe=False, content_type='application/json', status=400)