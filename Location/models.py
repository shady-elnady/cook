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


# Create your mofrom django.utils.text import slugify


class Location(Model):
    address = CharField(
        max_length= 100,
        verbose_name= _("Address")
    )
    lat = FloatField(
        verbose_name= _("Lat"),
    )
    lang = FloatField(
        verbose_name= _("Lang"),
    )

    class Meta:
        verbose_name= _("Location")
        verbose_name_plural= _("Locations")

