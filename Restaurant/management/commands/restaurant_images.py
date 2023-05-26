import os
import shutil
import random

from django.core.management.base import BaseCommand
from django.core.management import call_command

from django.conf import settings




class Command(BaseCommand):
    help = "Creates initial Restaurant models"
    
    def handle(self, *args, **options):      

        # Copy images from settings.BASE_DIR/Restaurant/management/images/Logo to settings.MEDIA_ROOT
        for img in os.listdir(os.path.join(settings.BASE_DIR, "Restaurant", "management", "images", "Logo")):
            try:
                shutil.copy(
                    os.path.join(settings.BASE_DIR, "Restaurant", "management", "images", "Logo", img),
                    os.path.join(settings.MEDIA_ROOT, "images", "Logo", img),
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"ERROR in Copy Restaurants Images is : {e}")
                )
        # Copy images from settings.BASE_DIR/Restaurant/management/images/Logo to settings.MEDIA_ROOT
        for img in os.listdir(os.path.join(settings.BASE_DIR, "Restaurant", "management", "images", "RestaurantMealImage")):
            try:
                shutil.copy(
                    os.path.join(settings.BASE_DIR, "Restaurant", "management", "images", "RestaurantMealImage", img),
                    os.path.join(settings.MEDIA_ROOT, "images", "RestaurantMealImage", img),
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"ERROR in Copy Restaurants Images is : {e}")
                )

        self.stdout.write(
            self.style.SUCCESS("Successfully created initial Restaurant models")
        )
