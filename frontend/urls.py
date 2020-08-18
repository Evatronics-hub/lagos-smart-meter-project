from django.urls import path, include
from django.views.generic import TemplateView
from .auth import (
    user, staff
)

user_auth_patterns = [
    path('login/', user.login),
    path('register/', user.register),
]

staff_auth_patterns = [
    path('register/', staff.register),
]

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('dashboard', user.dashboard, name='dashboard'),
    path('accounts/staff/', include(staff_auth_patterns)),
    path('accounts/', include(user_auth_patterns)),
]