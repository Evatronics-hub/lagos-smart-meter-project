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
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'name'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email'] # Email & Password are required by default.

    objects = UserManager()

    def get_full_name(self):
        # The user is identified by their name address
        return self.name

    def get_short_name(self):
        # The user is identified by their name address
        return self.name

    def __str__(self):              # __unicode__ on Python 2
        return self.name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active