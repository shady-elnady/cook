import os
import shutil
import random

from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings
from Restaurant.models import Restaurant, UserRestaurant

from User.models import Profile, User


class Command(BaseCommand):
    help = "Creates initial Users models"

    def handle(self, *args, **options):   
        #
        User.objects.create_superuser(
            username= "Shady",
            email= "shadyelnady@gmail.com",
            password= "12345",
        )
        User.objects.create_superuser(
            username= "Mai",
            email= "m@gmail.com",
            password= "12345",
        )
        User.objects.create_superuser(
            username= "Khalid",
            email= "khalid@gmail.com",
            password= "12345",
        )
        
        for index, profile in enumerate(Profile.objects.all().order_by("created_date")):
            try:
                profile.image = f"images/Profile/{index+1}.png"
                profile.save()
                UserRestaurant(
                    user = profile.user,
                    restaurant = Restaurant.objects.get(id= 1),
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
            self.style.SUCCESS("Successfully created initial Users models")
        )
