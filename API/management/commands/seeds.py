import os
import shutil
import random

from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings


class Command(BaseCommand):
    help = "Creates initial models Seeds"

    def handle(self, *args, **options):       
        works = [
            "data_seeds",
            "images_seeds",
        ]
        for work in works:
            try:
                call_command(work)
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"{work} Failed  \n \t \t Error is: {e}")
                )
        
        self.stdout.write(
            self.style.SUCCESS("Successfully created initial models Seeds")
        )
