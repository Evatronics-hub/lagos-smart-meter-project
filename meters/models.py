from django.db import models
from django.conf import settings
from random import randint

# Create your models here.
def make_card_id():
    return randint(100, 9999)


class Meter(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    meter_id = models.IntegerField(verbose_name='Meter ID', default=make_card_id, editable=False, primary_key=True)
    customer_balance = models.DecimalField(verbose_name='Customer Balance', max_digits=20, decimal_places=2)

    def __str__(self):
        return  f'<meter - [{self.meter_id}]>'