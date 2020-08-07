from django.urls import path
from .views import (
    home, login, dashboard, register
)

urlpatterns = [
    path('', home),
    path('login', login),
    path('dashboard', dashboard),
    path('register', register),
]