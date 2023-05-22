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
from colorfield.fields import ColorField

from Utils.models import BaseModel, BaseModelImage, BaseModelName
from Location.models import Location
from Category.models import Category
from Meal.models import Meal
from Payment.models import Currency


# Create your mofrom django.utils.text import slugify


class Restaurant(BaseModelName):

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
    is_nearby = BooleanField(
        default= False,
        verbose_name= _("is Nearby"),
    )

    @property
    def users_choiced_count(self) -> int:
        return len(self.Choiced_Users)

    @property
    def Reviews(self) -> float:
        reviews = 0
        for user in self.Choiced_Users:
            reviews = reviews +user.review
        return reviews


    # @property
    # def is_Nearby(self):
    #     all_reviews = 0
    #     for user in self.Users :
    #         all_reviews = all_reviews + user.review
    #     return all_reviews/len(self.Users)

    class Meta:
        verbose_name= _("Restaurant")
        verbose_name_plural= _("Restaurants")


class Color(Model):
    color = ColorField(
        default=8,
        format="hexa",
        verbose_name= _("Color"),
    )

    class Meta:
        verbose_name= _("Color")
        verbose_name_plural= _("Colors")



class Gradient(Model):

    class GradientTypes(TextChoices):
        LinearGradient = "LG", _("LinearGradient")

    class Aligments(TextChoices):
        topRight = "TR", _("topRight")
        bottomLeft = "BL", _("bottomLeft")
        bottomRight = "BR", _("bottomRight")
        topLeft = "TL", _("topRight")
    
    gradient_type = CharField(
        max_length=2,
        null= True,
        blank= True,
        choices= GradientTypes.choices,
        verbose_name= _("Gradient Type"),
    )
    begin = CharField(
        max_length= 2,
        null= True,
        blank= True,
        choices= Aligments.choices,
        verbose_name= _("Begin"),
    )
    end = CharField(
        max_length= 2,
        null= True,
        blank= True,
        choices= Aligments.choices,
        verbose_name= _("End"),
    )
    colors_steps = ManyToManyField(
        Color,
        through= "ColorStep",
        verbose_name= _("Colors Steps"),
    )
    
    class Meta:
        verbose_name= _("Gradient")
        verbose_name_plural= _("Gradients")


class Logo(BaseModelImage):
    restaurant = OneToOneField(
        Restaurant,
        primary_key= True,
        on_delete=CASCADE,
        related_name= "Logo",
        verbose_name= _("Restaurant"),
    )
    color = ForeignKey(
        Color,
        null= True,
        blank= True,
        on_delete=CASCADE,
        related_name= "Logos",
        verbose_name= _("Color"),
    )
    gradient = ForeignKey(
        Gradient,
        null= True,
        blank= True,
        on_delete=CASCADE,
        related_name= "Logos",
        verbose_name= _("Gradient"),
    )
  
    class Meta:
        verbose_name= _("Logo")
        verbose_name_plural= _("Logos")


class ColorStep(Model):
    gradient = ForeignKey(
        Gradient,
        on_delete= CASCADE,
        verbose_name= _("Gradient"),
    )
    color = ForeignKey(
        Color,
        on_delete= CASCADE,
        related_name= "+",
        verbose_name= _("Color"),
    )
    step = FloatField(
        null= True,
        blank= True,
        verbose_name= _("Step"),
    )

    class Meta:
        verbose_name= _("Color Step")
        verbose_name_plural= _("Colors Steps")


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
    is_popular = BooleanField(
        default= False,
        verbose_name= _("is Popular"),
    )

    @property
    def is_Popular(self) -> bool:
        return False

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
    
    # @property
    # def is_popular(self) -> bool:
    #     return False
    
    @property
    def slug(self) -> str:
        return slugify(f"{self.pk}")
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