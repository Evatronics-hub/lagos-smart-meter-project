from random import randint
from os import urandom

from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.
def make_card_id():
    return randint(100, 9999)

def make_token():
    return abs(hash(urandom(10)))


class Meter(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    meter_id = models.IntegerField(verbose_name='Meter ID', default=make_card_id, editable=False, primary_key=True)
    meter_token = models.IntegerField(default=make_token, editable=False)
    customer_balance = models.DecimalField(verbose_name='Customer Balance', max_digits=20, decimal_places=2)

    def __str__(self):
        return  f'<meter - [{self.meter_id}]>'