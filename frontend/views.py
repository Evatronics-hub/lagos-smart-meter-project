from django.shortcuts import render, reverse
from django.http import HttpResponseBadRequest, HttpResponsePermanentRedirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    if request.user.is_stake_holder or request.user.is_admin:
        return HttpResponsePermanentRedirect('/admin')
    try:
        balance = request.user.meter.customer_balance
        billing_type = request.user.meter.billing_type
    except:
        return HttpResponseBadRequest('User has no meter')
    context = {
        'balance' : balance,
        'billing_type' : billing_type
    }
    return render(request, 'dashboard.html', context=context)