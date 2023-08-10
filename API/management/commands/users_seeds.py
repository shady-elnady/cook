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
        User.objects.all().delete()
        users_data= [        
            {
                "username": "Shady",
                "email": "shadyelnady0@gmail.com",
                "password": "12345",
            },
            {
                "username": "Mai",
                "email": "m@gmail.com",
                "password": "12345",
            },
            {
                "username": "Khalid",
                "email": "khalid@gmail.com",
                "password": "12345",
            },
        ]
        
        for user in users_data:
            try:
                User.objects.create_superuser(
                    username= user["username"],
                    email= user["email"],
                    password= user["password"],
                )
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully Add User > {user}")
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"Error in User > {e}")
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
