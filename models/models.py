from django.db import models

# Create your models here.

class Meter(models.Model):
    meter-no = models.IntegerField(primary_key=True)
    balance = models.DecimalField(decimal_places=2, max_digits=100)

    def __str__(self):
        return f"Meter - {meter-no}"