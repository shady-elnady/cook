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
       
        ##
        load_data = [
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
        User.objects.create_superuser(
            username= "Shady",
            email= "shadyelnady@gmail.com",
            password= "12345",
        )
        User.objects.create_user(
            username= "M",
            email= "m@gmail.com",
            password= "12345",
        )
        #
        for index, profile in enumerate(Profile.objects.all().order_by("created_at")):
            try:
                profile.image = f"images/Profile/{index}.png"
                profile.save()
                UserRestaurant(
                    user = profile.user,
                    restaurant = 1,
                    is_favorite = True,
                    comment = "Food, as always, is good both upstairs and downstairs is always clean (download the bk app for deals etc.) sit upstairs every time, more relaxed feel.",
                    review = 4.5,
                    likes = 4,
                ).save()
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"Error in Profile > {e}")
                )
        
        self.stdout.write(
            self.style.SUCCESS("Successfully created initial models")
        )