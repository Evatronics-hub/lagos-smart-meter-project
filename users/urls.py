from django.urls import path
from .api import (
    UserRegisterAPI,
    UserDetailAPI,
    UserListAPI,
    LoginAPI,
    StakeHolderAPI
)

urlpatterns = [
    path('register', UserRegisterAPI.as_view()),
    path('login', LoginAPI.as_view()),
    path('users', UserListAPI.as_view()),
    path('users/<int:pk>', UserDetailAPI.as_view()),
    path('stakeholders', StakeHolderAPI.as_view()),
]