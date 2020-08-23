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
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)

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

    def save(self, *args, **kwargs):
        self.user.stake_holder = True
        self.user.save()
        super().save(*args, **kwargs)