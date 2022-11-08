from django.contrib.auth import models as auth_models
from django.db import models

from auth_demo.auth_app.managers import AppUserManager


# Create your models here.

# ~Proxy~
# class AppUser(auth_models.User):
#     def has_email(self):
#         return self.email or False
#
#     class Meta:
#         proxy = True

# ~Extending AbstractUser~
# class AppUser(AbstractUser):
#     age = models.PositiveIntegerField()


# ~Extending AbstractBaseUser~
class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )

    # User credentials consist of 'email' and 'password'
    USERNAME_FIELD = 'email'

    objects = AppUserManager()

    def has_email(self):
        return self.email or False


class Profile(models.Model):
    first_name = models.CharField(
        max_length=25,
    )

    last_name = models.CharField(
        max_length=25,
    )

    age = models.PositiveIntegerField()

    user = models.OneToOneField(
        AppUser,
        primary_key=True,
        on_delete=models.CASCADE,
    )
