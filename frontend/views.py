from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView

# Create your views here.

def home(request):
    return render(request, 'index.html')

def chart(request):
    return render(request, 'chart.html')

def dashboard(request):
    return HttpResponse('Hello from dashboard route')
    
def login(request):
    return HttpResponse('Hello from login route')
    
def register(request):
    return HttpResponse('Hello from register route')
    