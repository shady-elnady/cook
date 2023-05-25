import os
import shutil
import random

from django.core.management.base import BaseCommand
from django.core.management import call_command

from django.conf import settings


class Command(BaseCommand):
    help = "Creates initial Restaurant models"

    directory = os.path.join(settings.MEDIA_ROOT, "images", "Logo")

    # Check if the directory exists
    if not os.path.exists(directory):
        # If it doesn't exist, create it
        os.makedirs(directory)

    def handle(self, *args, **options):
        load_data = [
            "colors.json"
            "gradients.json",
            "color_steps.json",
            "restaurants.json",
            "logos.json",
        ]

        # Copy images from settings.BASE_DIR/main/static/img to settings.MEDIA_ROOT
        for img in os.listdir(os.path.join(settings.BASE_DIR, "Restaurant", "management", "images")):
            try:
                shutil.copy(
                    os.path.join(settings.BASE_DIR, "Restaurant", "management", "images", img),
                    os.path.join(settings.MEDIA_ROOT, "images", "Logo", img),
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"ERROR in Copy Restaurants Images is : {e}")
                )

        for data in load_data:
            try:
                call_command("loaddata", data)
            except Exception as e :
                self.stdout.write(
                    self.style.ERROR(f"{data} ERROR is : {e}")
                )

        self.stdout.write(
            self.style.SUCCESS("Successfully created initial Restaurant models")
        )
