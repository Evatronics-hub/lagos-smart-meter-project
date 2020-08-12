from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.response import Response
from users.serializers import UserSerializer
from knox.models import AuthToken 
from django.conf import settings
from users.models import User
from users.serializers import (
    LoginSerializer,
    RegisterSerializer,
    UserSerializer
)

# Create your views here.

class UserListAPI(generics.ListAPIView):
    ''' This will get all the users in for the Admin '''
    name = 'Users List'
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.IsAdminUser,
    ]


class UserDetailAPI(generics.RetrieveUpdateAPIView):
    ''' Provide the user full details '''
    name = 'User Detail'
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]


class UserRegisterAPI(generics.GenericAPIView):
    name = 'User Create'
    queryset = get_user_model().objects.all()
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'user' : self.serializer_class(user, context=self.get_serializer_context()).data ,
            'token' : AuthToken.objects.create(user)[1]
        })


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            'user' : UserSerializer(user, context=self.get_serializer_context()).data ,
            'token' : AuthToken.objects.create(user)[1]
        })