import os
import shutil
import random

from django.core.management.base import BaseCommand
from django.core.management import call_command

from django.conf import settings


class Command(BaseCommand):
    help = "Creates initial Profile Images models"

    def handle(self, *args, **options):
     

        # Copy images from settings.BASE_DIR/main/static/img to settings.MEDIA_ROOT
        for img in os.listdir(os.path.join(settings.BASE_DIR, "User", "management", "images", "Profile")):
            try:
                shutil.copy(
                    os.path.join(settings.BASE_DIR, "User", "management", "images", "Profile", img),
                    os.path.join(settings.MEDIA_ROOT, "images", "Profile", img),
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"ERROR in Copy Profiles Images is : {e}")
                )

        self.stdout.write(
            self.style.SUCCESS("Successfully created initial Profile Images models")
        )
