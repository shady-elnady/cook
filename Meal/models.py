from django.db import models
from django.db.models import (
    Model, AutoField, TextChoices,
    OneToOneField, FloatField,
    URLField,BooleanField, CharField,
    ForeignKey, DateField, EmailField,
    DateTimeField, ImageField,
    SET_NULL, CASCADE,
)
from django.utils.translation import gettext_lazy as _

from Utils.models import  BaseModelName
from Category.models import Category

# Create your mofrom django.utils.text import slugify


class Meal(BaseModelName):
    category = ForeignKey(
        Category,
        on_delete= CASCADE,
        related_name= "Items",
        verbose_name= _("Category"),
    )

    class Meta:
        verbose_name= _("Meal")
        verbose_name_plural= _("Meals")


