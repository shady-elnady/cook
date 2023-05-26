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
from os.path import join

# Create your models here.


def upload_to(instance, filename):
    extention= filename.split(".")[-1]
    imgName= getattr(instance, f'{instance.id}', f'{instance.pk}')
    newName= f"{imgName}.{extention}"    
    return join(f"images/{instance.__class__.__name__}/", newName)


class BaseModel(Model):
    id = AutoField(
        primary_key= True,
        verbose_name= _("ID"),
    )
    created_date= DateTimeField(
        auto_now_add=True,
        editable=False,
        blank=True,
        null=True,
        verbose_name= _("Created Date"),
    )
    last_updated= DateTimeField(
        auto_now=True,
        editable=False,
        blank=True,
        null=True,
        verbose_name= _("Last Update"),
    )

    @property
    def slug(self) -> str:
        return slugify(f"{self.id}")

    class Meta:
        ordering = ('-last_updated',)
        abstract= True


class BaseModelName(BaseModel):
    name = CharField(
        max_length= 15,
        verbose_name= _("Name"),
    )

    @property
    def slug(self) -> str:
        return slugify(f"{self.id}")

    def __str__(self) -> str:
        return f"{self.name}"

    def __decode__(self) -> str:
        return f"{self.name}"

    class Meta:
        abstract= True


class BaseModelNative(BaseModelName):
    native= CharField(
        max_length=20,
        unique=True,
        null=True,
        blank=True,
        verbose_name=_("Native"),
    )

    class Meta:
        abstract= True


class BaseModelImage(Model):
    image= ImageField(
        upload_to= upload_to,
        default= "images/{instance.__class__.__name__}/default.jpg' %}",
        null= True,
        blank= True,
        verbose_name= _("Image"),
    )
 
    class Meta:
        abstract= True


