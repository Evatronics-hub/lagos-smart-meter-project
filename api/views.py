from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth import get_user_model

from .serializers import (
    MeterSerializer, Meter,
)

# Create your views here.

class MeterAPIView(generics.ListAPIView):
    queryset = Meter.objects.all()
    serializer_class = MeterSerializer

class MeterRetrieveAPIView(generics.RetrieveUpdateAPIView):
    queryset = Meter.objects.all()
    serializer_class = MeterSerializer