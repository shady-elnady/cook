import os
import shutil
import random

from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = "Creates initial models"

    def handle(self, *args, **options):

        works = [
            "makemigrations",
            "migrate",
            "category_seeds",
            ("loaddata", "categories.json"),
        ]
        
        for work in works:
            try:
                call_command(work)
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"Failed to create {work} \n \t Error is: {e}")
                )
        # call_command("makemigrations")
        # call_command("migrate")
        # # call_command("loaddata", "db_user_fixture.json")
        # call_command("category_seeds")

        # call_command("loaddata", "categories.json")

        self.stdout.write(
            self.style.SUCCESS("Successfully created initial models")
        )
