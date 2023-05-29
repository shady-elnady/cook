import os
import shutil
import random

from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings
from Restaurant.models import UserRestaurant

from User.models import Profile, User


class Command(BaseCommand):
    help = "Creates initial models"

    def handle(self, *args, **options):   
        works = [
            "makemigrations",
            "migrate",
            # "createsuperuser",
            "collectstatic",
        ]
        for work in works:
            try:
                call_command(work)
                self.stdout.write(
            self.style.SUCCESS(f"Successfully {work}")
        )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"{work} Failed  \n \t \t Error is: {e}")
                )
        
        ##
        load_data = [
            "languages.json",
            "currencies.json",
            "countries.json",
            "governorates.json",
            "cities.json",
            "categories.json",
            "meals.json",
            "drivers.json",
            "hospitalities.json",
            "colors.json",
            "gradients.json",
            "color_steps.json",
            "logos.json",
            "restaurants.json",
            "restaurant_meals.json",
            "restaurant_meal_images.json",
            "restaurant_meal_sizes.json",
            "users.json",
        ]
        for data in load_data:
            try:
                call_command("loaddata", data)
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully {data} Load Data")
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"Load Data Failed from {data} , \n \t Error is: \t \t{e}")
                )
        ##
        call_command("users_seeds")
       
        self.stdout.write(
            self.style.SUCCESS("Successfully created initial models")
        )
