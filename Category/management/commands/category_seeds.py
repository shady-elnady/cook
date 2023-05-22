import os
import shutil
import random

from django.core.management.base import BaseCommand
from django.core.management import call_command

from django.conf import settings

from Category.models import Category


class Command(BaseCommand):
    help = "Creates initial Category models"

    def handle(self, *args, **options):
        imgs = []

        # Copy images from settings.BASE_DIR/main/static/img to settings.MEDIA_ROOT
        for img in os.listdir(os.path.join(settings.BASE_DIR, "Category", "management", "images")):
            shutil.copy(
                os.path.join(settings.BASE_DIR, "Category", "management", "images", img),
                os.path.join(settings.MEDIA_ROOT, "images", "Category", img),
            )
            imgs.append(img)

        # Create initial Category models from images, using ImageField

        # for img in imgs:
        #     try:
        #         Category.objects.create(
        #             name=img.split(".")[0],
        #             image=f"images/Category/{img}",
        #         )
        #     except Exception as e:
        #         self.stdout.write(
        #             self.style.ERROR(f"Failed to create initial Product model: {e}")
        #         )
        call_command("makemigrations")
        call_command("migrate")
        # call_command("loaddata", "db_user_fixture.json")
        call_command("category_seeds")

        call_command("loaddata", "categories.json")

        self.stdout.write(
            self.style.SUCCESS("Successfully created initial Product models")
        )
