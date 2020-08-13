from rest_framework import serializers
from meters.models import Meter
from django.contrib.auth import get_user_model

class MeterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meter
        fields = ('user', 'meter_id', 'customer_balance', )
    
class UpdateMeterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meter
        fields = ('user', 'meter_id', 'customer_balance', )
        extra_kwargs = {'user' : {'read_only' : True } }