from django.urls import path, include
from django.views.generic import TemplateView
from .views import dashboard
from .auth import (
    user, staff
)

user_auth_patterns = [
    path('login/', user.login, name='login'),
    path('register/', user.register, name='register'),
    path('meters/', user.meter, name='register_meter')
]

staff_auth_patterns = [
    path('register/', staff.register),
]

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('dashboard', dashboard, name='dashboard'),
    path('accounts/staff/', include(staff_auth_patterns)),
    path('accounts/', include(user_auth_patterns)),
]