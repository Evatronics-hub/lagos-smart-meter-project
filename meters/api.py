from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth import get_user_model
from meters.models import Meter, Billing
from rest_framework import permissions

from .serializers import (
    MeterSerializer, 
    UpdateMeterSerializer,
    BillingSerializer,
)

class MeterAPIView(generics.ListCreateAPIView):
    queryset = Meter.objects.all()
    serializer_class = MeterSerializer


class MeterRetrieveAPIView(generics.RetrieveUpdateAPIView):
    queryset = Meter.objects.all()
    serializer_class = UpdateMeterSerializer

class BillingAPIView(generics.ListCreateAPIView):
    queryset = Billing.objects.all()
    serializer_class = BillingSerializer
    # permission_classes = [
    #     permissions.IsAdminUser
    # ]

class BillingRetrieveAPIView(generics.RetrieveUpdateAPIView):
    queryset = Billing.objects.all()
    serializer_class = BillingSerializer
    # permission_classes = [
    #     permissions.IsAdminUser
    # ]