from django.db import models
from django.db.models import (
    Model, AutoField, TextChoices,
    OneToOneField, FloatField,
    URLField,BooleanField, CharField,
    ForeignKey, DateField, EmailField,
    DateTimeField, ImageField, ManyToManyField,
    SET_NULL, CASCADE, TimeField,
)
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from Location.models import Location

from Utils.models import BaseModel, BaseModelImage, BaseModelName
from Category.models import Category
from Meal.models import Meal
from Payment.models import Currency


# Create your mofrom django.utils.text import slugify


class Restaurant(BaseModelName, BaseModelImage):

    class RestaurantTypes(TextChoices):
        C = "C", _("Coffee")
        F = "F", _("Fast Food")
    
    is_best = BooleanField(
        default= False,
        verbose_name= _("is Best"),
    )
    free_shipping = FloatField(
        verbose_name= _("Free shipping"),
    )
    type = CharField(
        max_length= 2,
        choices= RestaurantTypes.choices,
        verbose_name= _("Restaurant Type")
    )
    open_time = TimeField(
        verbose_name= _("Open Time"),
    )
    close_time = TimeField(
        verbose_name= _("Close Time"),
    )
    location = ForeignKey(
        Location,
        on_delete= CASCADE,
        related_name= "Profiles",
        verbose_name= _("Location"),
    )

    # @property
    # def reviews(self):
    #     all_reviews = 0
    #     for user in self.Users :
    #         all_reviews = all_reviews + user.review
    #     return all_reviews/len(self.Users)
    
    # @property
    # def Categories(self):
    #     categories_list = []
    #     for Meal in self.Meals :
    #         categories_list.append(Meal.category)
    #     return categories_list

    class Meta:
        verbose_name= _("Restaurant")
        verbose_name_plural= _("Restaurants")


class RestaurantMeal(Model):
    restaurant = ForeignKey(
        Meal,
        on_delete=CASCADE,
        related_name= "Restaurant_Meals",
        verbose_name= _("Restaurant"),
    )
    meal = ForeignKey(
        Meal,
        on_delete=CASCADE,
        related_name= "Restaurants",
        verbose_name= _("Meal"),
    )

    @property
    def slug(self) -> str:
        return slugify(f"{self.pk}")
    
    class Meta:
        unique_together = (
            "restaurant",
            "meal",
        )
        verbose_name= _("Restaurant Meal")
        verbose_name_plural= _("Restaurants Meals")



class RestaurantMealSize(BaseModel):

    class Sizes(TextChoices):
        L = "L", _("L")
        M = "M", _("M")
        S = "S", _("S")
   
    restaurant_Meal = ForeignKey(
        RestaurantMeal,
        on_delete= CASCADE,
        related_name= "Restaurant_Meals_Sizes",
        verbose_name= _("Restaurant Meal"),
    )
    size = CharField(
        max_length= 2,
        choices= Sizes.choices,
        verbose_name= _("Size"),
    )
    price = FloatField(
        verbose_name= _("Price"),
    )
    currency = ForeignKey(
        Currency,
        on_delete= CASCADE,
        related_name= _("Meals+"),
        verbose_name= _("Currency"),
    )
    
    @property
    def slug(self) -> str:
        return slugify(f"{self.pk}")

    class Meta:
        verbose_name= _("Restaurant Meal Size")
        verbose_name_plural= _("Restaurants Meals Sizes")


class RestaurantMealImage(BaseModelImage):
    restaurant_meal = ForeignKey(
        RestaurantMeal,
        on_delete= CASCADE,
        related_name= "Images",
        verbose_name= _("Restaurant Meal"),
    )
    
    @property
    def slug(self) -> str:
        return slugify(f"{self.pk}")

    class Meta:
        verbose_name= _("Restaurant Meal Image")
        verbose_name_plural= _("Restaurant Meals Images")