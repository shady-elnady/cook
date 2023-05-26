import os
import shutil
import random

from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings


def mkDir(directory):
    try:
        if not os.path.exists(directory):
            # If it doesn't exist, create it
            os.makedirs(directory)
    except Exception as e:
        print(f"Error in Make Directory is : {e}")

class Command(BaseCommand):
    help = "Creates initial models"

    def handle(self, *args, **options):

        mkDir(os.path.join(settings.BASE_DIR, "DataBase"))
        mkDir(os.path.join(settings.BASE_DIR, "media"))
        mkDir(os.path.join(settings.BASE_DIR, "static"))
        mkDir(os.path.join(settings.BASE_DIR, "staticfiles"))
        mkDir(os.path.join(settings.MEDIA_ROOT, "media", "images"))
        mkDir(os.path.join(settings.MEDIA_ROOT, "media", "images", "Logo"))
        mkDir(os.path.join(settings.MEDIA_ROOT, "media", "images", "Category"))
        mkDir(os.path.join(settings.MEDIA_ROOT, "media", "images", "Profile"))
        mkDir(os.path.join(settings.MEDIA_ROOT, "media", "images", "RestaurantMealImage"))

        ###
        load_images = [
            "category_images",
            "profile_images",
            "driver_images",
            "restaurant_images",
        ]

        for img in load_images:
            try:
                call_command(img)
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"{img} Load Data Failed , \n \t \t Error is: {e}")
                )
       
        
        self.stdout.write(
            self.style.SUCCESS("Successfully created initial models")
        )
