from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import (
    render, HttpResponse, HttpResponseRedirect,
    reverse
)

from .forms import StaffForm

def register(request):
    ''' This will register a normal a user '''
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return HttpResponseRedirect(reverse('dashboard'))
    else:
        form = StaffForm
    return render(request, 'auth/staff/signup.html', {'form': form})