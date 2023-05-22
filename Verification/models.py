from django.db import models
from django.db.models import (
    Model, TextChoices, IntegerField,
    OneToOneField, FloatField, TextField,
    URLField,BooleanField, CharField,
    ForeignKey, DateField, EmailField,
    DateTimeField, ImageField, SmallIntegerField,
    SET_NULL, CASCADE, ManyToManyField,
)
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.conf import settings

from datetime import date
import calendar
from os.path import join

# Create your models here.

# this model Stores the data of the Phones Verified


class PhoneModel(Model):
    owner = OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete= CASCADE,
        related_name= "Mobile",
        verbose_name= _("Owner")
    )
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
    )
    mobile = CharField(
        validators=[phone_regex],
        max_length=17,
        blank=True,
        null= True,
        verbose_name= _("Mobile"),
    ) # Validators should be a list
    # mobile = IntegerField(
    #     blank=False,
    #     verbose_name= _("Mobile"),
    # )
    is_verified = BooleanField(
        blank=False,
        default=False,
        verbose_name= _("is Verified"),
    )
    counter = IntegerField(
        default=0,
        blank=False,
        verbose_name= _("Counter"),
    )   # For HOTP Verification

    @property
    def slug(self):
        return slugify(str(self.pk))

    def __str__(self):
        return str(self.mobile)

    def __decode__(self):
        return f"{self.mobile}"    

    class Meta:
        verbose_name = _("Phone Model")
        verbose_name_plural = _("Phones Models")
