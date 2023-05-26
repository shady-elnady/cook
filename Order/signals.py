from django.db.models.signals import post_save
from django.dispatch import receiver
from django.apps import apps
from django.contrib.auth import get_user_model
from django.core.signals import setting_changed
from django.test import override_settings
from django.conf import settings
from rest_framework.authtoken.models import Token

from .models import OrderMeal


## Signal to Create Profile for each new User
@receiver(post_save, sender=OrderMeal)
def add_popular_meal(sender, instance, created, **kwargs):
    if created:
        restaurant_meal = instance.meal.restaurant_Meal
        restaurant_meal.orders_count = 1+ restaurant_meal.orders_count
        restaurant_meal.save()
