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
    
    def update(self, instance, validated_data):
        instance.billing_type = validated_data.get('billing_type', instance.billing_type)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        amount = 0
        if (amount := validated_data.get('customer_balance', None)):
            divisor = instance.billing_type.price_per_unit
            amount = amount / divisor
        instance.customer_balance += amount
        instance.save()
        return instance
    

class BillingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Billing
        fields = '__all__'