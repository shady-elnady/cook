from django.db import models
from django.db.models import (
    Model, AutoField, TextChoices,
    OneToOneField, FloatField,
    URLField,BooleanField, CharField,
    ForeignKey, DateField, EmailField, TextField,
    DateTimeField, ImageField, ManyToManyField,
    SET_NULL, CASCADE, TimeField, SmallIntegerField,
)
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from datetime import datetime
from colorfield.fields import ColorField

from Address.models import Address
from User.models import User
from Utils.models import BaseModel, BaseModelImage, BaseModelName
from Category.models import Category
from Meal.models import Meal
from Payment.models import Currency


# Create your mofrom django.utils.text import slugify


class Hospitality(BaseModelName):
    class Meta:
        verbose_name= _("Hospitality")
        verbose_name_plural= _("Hospitalities")




class Gradient(Model):

    class GradientTypes(TextChoices):
        LinearGradient = "LG", _("LinearGradient")

    id = AutoField(
        primary_key= True,
        verbose_name= _("ID"),
    )
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
    
    class Meta:
        verbose_name= _("Gradient")
        verbose_name_plural= _("Gradients")


class Logo(BaseModelImage):
    id = AutoField(
        primary_key= True,
        verbose_name= _("ID"),
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


class Restaurant(BaseModelName):

    class RestaurantTypes(TextChoices):
        C = "C", _("Coffee")
        F = "F", _("Fast Food")
   
    free_shipping = FloatField(
        verbose_name= _("Free shipping"),
    )
    type = CharField(
        max_length= 2,
        choices= RestaurantTypes.choices,
        verbose_name= _("Restaurant Type")
    )
    open_time = TimeField(
        null= True,
        blank= True,
        verbose_name= _("Open Time"),
    )
    close_time = TimeField(
        null= True,
        blank= True,
        verbose_name= _("Close Time"),
    )
    address = ForeignKey(
        Address,
        on_delete= CASCADE,
        null= True,
        blank= True,
        related_name= "Restaurants",
        verbose_name= _("Address"),
    )
    logo = OneToOneField(
        Logo,
        on_delete=CASCADE,
        related_name= "Restaurant",
        verbose_name= _("Logo"),
    )
    hospitalities = ManyToManyField(
        Hospitality,
        verbose_name= _("Hospitalities")
    )
    categories = ManyToManyField(
        Category,
        verbose_name= _("Categories")
    )
   
    # @property
    # def users_choiced_count(self) -> int:
    #     return len(self.Choiced_Users)

    # @property
    # def is_Opened(self):
    #     return True
    #     # return self.close_time > datetime.now().time() > self.open_time 
    # # datetime.now().strftime('%H:%M:%S')
    
    # @property
    # def Likes(self) -> int:
    #     likes = 0
    #     for user in self.Choiced_Users:
    #         likes = likes + user.likes
    #     return int(likes/len(self.Choiced_Users))

    # @property
    # def Reviews(self) -> float:
    #     reviews = 0
    #     for user in self.Choiced_Users:
    #         reviews = reviews + user.review
    #     return reviews/len(self.Choiced_Users)

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
    id = AutoField(
        primary_key= True,
        verbose_name= _("ID"),
    )
    color = ColorField(
        default=8,
        format="hexa",
        unique= True,
        verbose_name= _("Color"),
    )

    class Meta:
        verbose_name= _("Color")
        verbose_name_plural= _("Colors")


class ColorStep(Model):
    id = AutoField(
        primary_key= True,
        verbose_name= _("ID"),
    )
    gradient = ForeignKey(
        Gradient,
        on_delete= CASCADE,
        related_name= "Colors_Steps",
        verbose_name= _("Gradient"),
    )
    color = ForeignKey(
        Color,
        on_delete= CASCADE,
        related_name= "Colors_Steps",
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


class RestaurantMeal(BaseModelName):
    restaurant = ForeignKey(
        Restaurant,
        on_delete=CASCADE,
        related_name= "Restaurant_Meals",
        verbose_name= _("Restaurant"),
    )
    meal = ForeignKey(
        Meal,
        on_delete=CASCADE,
        related_name= "Restaurant_Meals",
        verbose_name= _("Meal"),
    )
    orders_count = SmallIntegerField(
        null= True,
        blank= True,
        editable= False,
        verbose_name= _("Order Count"),
    )

    # @property
    # def primary_image(self):
    #     return self.Images[0]
    
    # @property
    # def is_Popular(self) -> int:
    #     return self.Restaurant_Meals_Sizes

    @property
    def slug(self) -> str:
        return slugify(f"{self.pk}")
    
    class Meta:
        ordering = ["last_updated"]
        verbose_name= _("Restaurant Meal")
        verbose_name_plural= _("Restaurants Meals")



class RestaurantMealSize(BaseModel):

    class Sizes(TextChoices):
        L = "L", _("L")
        M = "M", _("M")
        S = "S", _("S")
   
    restaurant_meal = ForeignKey(
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


class UserRestaurant(BaseModel):
    user = ForeignKey(
        User,
        on_delete= CASCADE,
        related_name= "User_Restaurants",
        verbose_name= _("User"),
    )
    restaurant = ForeignKey(
        Restaurant,
        on_delete= CASCADE,
        related_name= "Choiced_Users",
        verbose_name= _("Restaurant"),
    )
    is_favorite = BooleanField(
        default= False,
        verbose_name= _("is Favorite"),
    )
    comment = TextField(
        verbose_name= _("Comment"),
    )
    review = FloatField(
        verbose_name= _("Review"),
    )
    likes = SmallIntegerField(
        default= 0,
        verbose_name= _("Likes"),
    )

    @property
    def slug(self):
        return slugify(str(self.pk))

    class Meta:
        unique_together = (
            "user",
            "restaurant",
        )
        verbose_name = _("User Restaurant")
        verbose_name_plural = _("Users Restaurants")
