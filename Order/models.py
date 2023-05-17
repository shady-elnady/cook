from django.db import models
from django.db.models import (
    Model, TextChoices,
    OneToOneField, FloatField, TextField,
    URLField,BooleanField, CharField,
    ForeignKey, DateField, EmailField,
    DateTimeField, ImageField, SmallIntegerField, PositiveSmallIntegerField,
    SET_NULL, CASCADE, ManyToManyField,
)
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from Driver.models import Driver
from Payment.models import PaymentMethod

from Utils.models import BaseModel
from Restaurant.models import Restaurant, RestaurantMealSize


# Create your mofrom django.utils.text import slugify


class Order(BaseModel):
    user = ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete= CASCADE,
        related_name= "Orders",
        verbose_name= _("User"),
    )
    payment_method = ForeignKey(
        PaymentMethod,
        on_delete= CASCADE,
        related_name= "Orders",
        verbose_name= _("Payment Method"),
    )

    # @property
    # def Total_order_price(self) -> float:
    #     total = 0
    #     for meal in self.Order_Meals :
    #         total = total + meal.Total_meal_price()
    #     return total

    class Meta:
        verbose_name= _("Order")
        verbose_name_plural= _("Orders")


class OrderMeal(BaseModel):
    order = ForeignKey(
        Order,
        on_delete= CASCADE,
        related_name= "Order_Meals",
        verbose_name= _("Order"),
    )
    meal = ForeignKey(
        RestaurantMealSize,
        on_delete= CASCADE,
        related_name= "Orders",
        verbose_name= _("Meal"),
    )
    quantity = PositiveSmallIntegerField(
        verbose_name= _("Quantity"),
    )

    # @property
    # def Total_meal_price(self) -> float:
    #     return self.meal.price * self.quantity

    class Meta:
        unique_together = (
            "order",
            "meal",
        )
        verbose_name= _("Order Meal")
        verbose_name_plural= _("Orders Meals")



class OrderRateDriver(BaseModel):
    order = OneToOneField(
        Order,
        on_delete= CASCADE,
        related_name= "Order_Rate_Driver",
        verbose_name= _("Order"),
    )
    driver = ForeignKey(
        Driver,
        on_delete= CASCADE,
        related_name= "Orders",
        verbose_name= _("Driver"),
    )
    reviews = FloatField(
        verbose_name= _("Reviews"),
    )
    comment = TextField(
        max_length= 200,
        verbose_name= _("Comment"),
    )
    is_good_service = BooleanField(
        verbose_name= _("is Good Service"),
    )
    is_on_time = BooleanField(
        verbose_name= _("is On Time"),
    )
    is_clean = BooleanField(
        verbose_name= _("is Clean"),
    )
    is_carefull = BooleanField(
        verbose_name= _("is Carefull"),
    )
    is_work_hard = BooleanField(
        verbose_name= _("is Work Hard"),
    )
    is_polite = BooleanField(
        verbose_name= _("is Polite"),
    )

    class Meta:
        unique_together = (
            "order",
            "driver",
        )
        verbose_name= _("Order Rate Driver")
        verbose_name_plural= _("Orders Rate Drivers")


class OrderRateRestaurant(BaseModel):
    order = OneToOneField(
        Order,
        related_name= "Order_Rate_Restaurant",
        on_delete= CASCADE,
        verbose_name= _("Order"),
    )
    restaurant = ForeignKey(
        Restaurant,
        on_delete= CASCADE,
        related_name= _("Orders"),
        verbose_name= _("Restaurant"),
    )
    reviews = FloatField(
        verbose_name= _("Reviews"),
    )
    comment = TextField(
        max_length= 500,
        verbose_name= _("Comment"),
    )
    is_good_package = BooleanField(
        verbose_name= _("is Good package"),
    )
    is_clean = BooleanField(
        verbose_name= _("is Clean"),
    )
    is_pair_price = BooleanField(
        verbose_name= _("is pair_price"),
    )    

    class Meta:
        unique_together = (
            "order",
            "restaurant",
        )
        verbose_name= _("Order Rate Restaurant")
        verbose_name_plural= _("Orders Rate Restaurants")
