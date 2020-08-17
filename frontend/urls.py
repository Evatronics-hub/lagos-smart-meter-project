from django.urls import path
from .views import (
    home, login, dashboard, register,
    chart
)

urlpatterns = [
    path('', home),
    path('login', login),
    path('dashboard', dashboard),
    path('charts/meters', chart),
    path('register', register),
]