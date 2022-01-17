from datetime import timedelta

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
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

class UserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'W'

    GENDER_CHOICES = (
        (MALE, 'M'),
        (FEMALE, 'Ж')
    )

    user = models.OneToOneField(ShopUser, unique=True, null=False, db_index=True, on_delete=models.CASCADE)
    abiut = models.TextField(verbose_name='о себе', blank=True, null=True)
    gender = models.CharField(verbose_name='пол', choices=GENDER_CHOICES, blank=True, max_length=2)

    @receiver(post_save, sender=ShopUser)
    def create_user_prifile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=ShopUser)
    def save_user_prifile(sender, instance, **kwargs):
        instance.userprofile.save()
