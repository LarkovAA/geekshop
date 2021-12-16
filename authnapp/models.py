from datetime import timedelta

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.utils.timezone import now


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='user avatar', blank=True)
    age = models.PositiveIntegerField(verbose_name='возраст', default=18)
    activation_key = models.CharField(max_length=120, blank=True)
    activation_key_expires = models.DateTimeField(auto_now=True, blank=True, null=True)

    def is_activation_key_expires(self):
        if now() <= self.activation_key_expires + timedelta(hours=48):
            return False
        return True