from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth import get_user_model
from meters.models import Meter
from rest_framework import permissions

from .serializers import (
    MeterSerializer, 
)

class MeterAPIView(generics.ListCreateAPIView):
    queryset = Meter.objects.all()
    serializer_class = MeterSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]

class MeterRetrieveAPIView(generics.RetrieveUpdateAPIView):
    queryset = Meter.objects.all()
    serializer_class = MeterSerializer