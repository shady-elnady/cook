from django.db import models
from django.db.models import (
    Model, AutoField, TextChoices,
    OneToOneField, FloatField,
    URLField,BooleanField, CharField,
    ForeignKey, DateField, EmailField,
    DateTimeField, ImageField,
    SET_NULL, CASCADE,
)
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from Utils.models import BaseModelName, BaseModelImage


# Create your mofrom django.utils.text import slugify


class Category(BaseModelName, BaseModelImage):

    class Meta:
        verbose_name= _("Category")
        verbose_name_plural= _("Categories")
