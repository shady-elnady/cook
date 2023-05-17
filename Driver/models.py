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
from django.core.validators import RegexValidator

from Utils.models import BaseModelImage, BaseModelName

# Create your mofrom django.utils.text import slugify


class Driver(BaseModelName, BaseModelImage):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
    )
    phone_number = CharField(
        validators=[phone_regex],
        max_length=17,
        blank=True,
        null= True,
        verbose_name= _("Phone Number"),
    ) # Validators should be a list

    class Meta:
        verbose_name= _("Driver")
        verbose_name_plural= _("Drivers")

