import os
import shutil
import random

from django.core.management.base import BaseCommand
from django.core.management import call_command

from django.conf import settings

class Command(BaseCommand):
    help = "Creates initial Category models"


    directory = os.path.join(settings.MEDIA_ROOT, "images", "Category")

    # Check if the directory exists
    if not os.path.exists(directory):
        # If it doesn't exist, create it
        os.makedirs(directory)

    def handle(self, *args, **options):

        # Copy images from settings.BASE_DIR/main/static/img to settings.MEDIA_ROOT
        for img in os.listdir(os.path.join(settings.BASE_DIR, "Category", "management", "images")):
            try:
                shutil.copy(
                    os.path.join(settings.BASE_DIR, "Category", "management", "images", img),
                    os.path.join(settings.MEDIA_ROOT, "images", "Category", img),
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"Failed Tranform Category Images \n \t Error is: {e}")
                )

        try:
            call_command("loaddata", "categories.json")
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f"Category Load Data Failed  \n \t Error is: {e}")
            )

        self.stdout.write(
            self.style.SUCCESS("Successfully created initial Category models")
        )
