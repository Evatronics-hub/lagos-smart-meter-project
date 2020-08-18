from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required

from users.forms import RegisterForm

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)
        if user and user is not None:
            auth_login(request, user)
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            raise ValueError
    return render(request, 'auth/login.html')


def register(request):
    ''' This will register a normal a user '''
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = RegisterForm
    return render(request, 'auth/signup.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'index.html')