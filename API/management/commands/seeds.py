import os
import shutil
import random

from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = "Creates initial models"

    def handle(self, *args, **options):
        ### 
        works = [
            "makemigrations",
            "migrate",
            "category_seeds"
            "restaurant_seeds",
        ]
        for work in works:
            try:
                call_command(work)
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"{work} Failed  \n \t \t Error is: {e}")
                )
        
        ###
        load_data = [
            "languages.json",
            "currencies.json",
            "countries.json",
            "governorates.json",
            "cities.json",
        ]
        for data in load_data:
            try:
                call_command("loaddata", data)
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"{data} Load Data Failed , \n \t \t Error is: {e}")
                )
        
        self.stdout.write(
            self.style.SUCCESS("Successfully created initial models")
        )
