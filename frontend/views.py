from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView

# Create your views here.

def home(request):
    return HttpResponse('Hello from home route')

def dashboard(request):
    return HttpResponse('Hello from dashboard route')
    
def login(request):
    return HttpResponse('Hello from login route')
    
def register(request):
    return HttpResponse('Hello from register route')
    