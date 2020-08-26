from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from .models import User

class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class StakeHolder(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'staff': True})
    role = models.ManyToManyField(Role)

    def __str__(self):
        return self.user.name

    @property
    def users(self):
        suffix = 'user'
        num = len(self.distributor.only())
        if num > 1:
            suffix = 'users'
        if num == 0:
            return 'No users yet'
        return f'{num} {suffix}'

    @property
    def name(self):
        return self.user.name

    @property
    def roles(self):
        roles = self.role.get_queryset()
        result = []
        for role in roles:
            result.append(role.name)
        return result

    @property
    def connected_meters(self):
        meters = self.distributor.only()
        total = 0
        for meter in meters:
            if meter.is_active:
               total += 1
        return total

    @property
    def total_revenue(self):
        meters = self.distributor.only()
        total = 0
        for meter in meters:
            total += meter.customer_balance
        return total

    def save(self, *args, **kwargs):
        self.user.stake_holder = True
        self.user.save()
        super().save(*args, **kwargs)