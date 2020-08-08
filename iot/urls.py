from django.urls import path
from .views import update_user_info

urlpatterns = [
    path('', update_user_info),
]