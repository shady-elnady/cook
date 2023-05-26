from django.db.models.signals import post_save
from django.dispatch import receiver
from django.apps import apps
from django.contrib.auth import get_user_model
from django.core.signals import setting_changed
from django.test import override_settings
from django.conf import settings
from rest_framework.authtoken.models import Token

from .models import User, Profile



## Signal to Create Profile for each new User
@receiver(post_save, sender=User)
def create_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)        
        Token.objects.create(user=instance)
    instance.Profile.save()


