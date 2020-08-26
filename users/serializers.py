from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import User
from .staff import StakeHolder

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id'
            ,'name'
            ,'email'
            ,'last_login',
        ]


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'name',
            'email',
            'password',
        )
        extra_kwargs = {
            'password' : {
                'write_only' : True
            }
        }
    
    def create(self, validated_data, *args, **kwargs):
        user = User.objects.create_user(
            validated_data['name']
            ,validated_data['email']
            ,validated_data['password']
        )
        return user


class LoginSerializer(serializers.Serializer):
    name = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user:
            return user
        raise serializers.ValidationError('Incorrect credentials. Try again')


class StakeHolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = StakeHolder
        fields = ('name', 'connected_meters', 'total_revenue', 'roles')