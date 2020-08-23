from random import randint
from os import urandom

from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from users.staff import StakeHolder

# Create your models here.
def make_card_id():
    return randint(100, 9999)

def make_token():
    return abs(hash(urandom(10)))

class Billing(models.Model):
    name = models.CharField(max_length=128)
    price_per_unit = models.DecimalField(decimal_places=2, max_digits=128)

    def __str__(self):
        return f'{self.name}'

class Meter(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    meter_id = models.IntegerField(verbose_name='Meter ID', default=make_card_id, editable=False, primary_key=True)
    meter_token = models.IntegerField(default=make_token, editable=False)
    customer_balance = models.IntegerField(verbose_name='Customer Balance')
    stake_holder = models.ForeignKey(StakeHolder, on_delete=models.CASCADE, related_name='distributor')
    billing_type = models.ForeignKey(Billing, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)

    def __init__(self, *args, **kwargs):
        self._init_balance = 0
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f'<meter - [{self.meter_id}]>'

    @property
    def balance(self):
        '''
        This is a temp variable that will help the IoT devices
        to update the value of the customer balance since it 
        is the actual unit spent, it doesn't need to be
        converted
        '''
        return self.customer_balance

    @balance.setter
    def balance(self, num):
        self._init_balance = self.customer_balance
        self._init_balance -= num

    def pay(self, *args, **kwargs):
        divisor = self.billing_type.price_per_unit
        num = self.customer_balance
        amount = num / divisor
        self.customer_balance = amount
        if self.customer_balance < -1:
            raise ValidationError('Amount exceeded')
        super().save(*args, **kwargs)

    def save_iot(self, *args, **kwargs):
        self.customer_balance = self._init_balance
        if self.customer_balance < -1:
            raise ValidationError('Amount exceeded')
        super().save(*args, **kwargs)