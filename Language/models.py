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

from Utils.models import BaseModelNative


# Create your mofrom django.utils.text import slugify


class Language(BaseModelNative):
    symbol = CharField(
        max_length= 15,
        unique= True,
        verbose_name= _("Symbol Code"),
    )
    emoji = CharField(
        max_length= 1,
        verbose_name= _("Emoji"),
    )
    rtl = BooleanField(
        default= False,
        verbose_name= _("Right To Left"),
    )

    @property
    def slug(self) -> str:
        return slugify(f"{self.id}")

    def __str__(self) -> str:
        return f"{self.native}"

    def __decode__(self) -> str:
        return f"{self.native}"

    class Meta:
        verbose_name= _("Language")
        verbose_name_plural= _("Languages")
