from rest_framework import serializers
from meters.models import Meter, Billing
from django.contrib.auth import get_user_model

class MeterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meter
        fields = ('user', 'meter_id', 'customer_balance', 'billing_type')
    
class UpdateMeterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meter
        fields = ('user', 'meter_id', 'customer_balance', 'billing_type', 'is_active')
        extra_kwargs = {'user' : {'read_only' : True } }


class BillingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Billing
        fields = '__all__'