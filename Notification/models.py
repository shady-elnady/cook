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

from Utils.models import BaseModel


# Create your mofrom django.utils.text import slugify


class Notification(BaseModel):

    class Meta:
        verbose_name= _("Notification")
        verbose_name_plural= _("Notifications")

