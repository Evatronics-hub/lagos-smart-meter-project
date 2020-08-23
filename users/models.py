from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, name, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not name:
            raise ValueError('Users must have a username')

        user = self.model(
            name=name,
            email=email,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, name, email, password, **extra_fields):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            name=name,
            email=email,
            password=password,
            **extra_fields
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, password, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """

        user = self.create_user(
            name=name,
            email=email,
            password=password,
            **extra_fields
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username_validator = UnicodeUsernameValidator()

    name = models.CharField(
        verbose_name='username',
        max_length=255,
        validators=[username_validator],
        unique=True,
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
    )
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    stake_holder = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'name'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    @property
    def is_stake_holder(self):
        return self.stake_holder