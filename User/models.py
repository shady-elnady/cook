from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.conf import settings

from datetime import date
import calendar
from os.path import join
from django.db.models import (
    Model, TextChoices, UUIDField,
    OneToOneField, FloatField, TextField,
    URLField,BooleanField, CharField,
    ForeignKey, DateField, EmailField,
    DateTimeField, ImageField, SmallIntegerField,
    SET_NULL, CASCADE, ManyToManyField, IntegerField, PositiveSmallIntegerField,
)
import uuid


from Location.models import Location
from Restaurant.models import Restaurant
from Utils.models import BaseModel, BaseModelImage
from Language.models import Language
from Address.models import Address
from .managers import UsersManager


# Create your models here.



class Age:
    def __init__(self, year, month, day):
        if ( year is None and month is None and day is None):
            return None
        self.year = year if year is not None else 0
        self.month = month if month is not None else 0
        self.day = day if day is not None else 0


class User(AbstractBaseUser, PermissionsMixin):

    USERNAME_FIELD = "username"      # e.g: "username", "email"
    EMAIL_FIELD = "email"         # e.g: "email", "primary_email"
    REQUIRED_FIELDS = ['password', "email"]

    objects = UsersManager()
    
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name= _("ID"),)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
    )
    mobile = CharField(
        max_length=17,
        unique= True,
        validators=[phone_regex],
        blank=True,
        null= True,
        verbose_name= _("mobile"),
    )
    otp = CharField(
        max_length=25,
        blank=True,
        null= True,
        verbose_name= _("OTP"),
    )
    email = EmailField(
        max_length=200,
        unique=True,
        error_messages={
            'unique': _('E-Mail Is User')
        },
        null=False,
        blank=False,
        verbose_name= _("E-Mail"),
    )
    username = CharField(
        max_length=30,
        unique=True,
         error_messages={
            'unique': _('User Name Is User. choose Another')
        },
        null=False,
        blank=False,
        verbose_name= _("User Name"),
    )
    is_active = BooleanField(
        default= False,
        verbose_name= _("is Active"),
    )
    is_verified = BooleanField(
        default= False,
        verbose_name= _("is Verfied"),
    )
    is_staff = BooleanField(
        default= False,
        verbose_name= _("is Staff"),
    )
    is_superuser = BooleanField(
        default=False,
        verbose_name= _("is Super User"),
    )
    
    @property
    def slug(self):
        return slugify(str(self.username))

    def __str__(self):
        return f"{self.username}"

    def __decode__(self):
        return f"{self.username}"    

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})


class Profile(BaseModel, BaseModelImage):

    class Genders(TextChoices):
        male = "M", _("Male")
        female = "F", _("Female")

    user = OneToOneField(
        settings.AUTH_USER_MODEL,
        # primary_key= True,
        on_delete=CASCADE,
        related_name= "profile",
        verbose_name= _("User"),
    )
    first_name = CharField(
        max_length=15,
        null= True,
        blank= True,
        verbose_name= _("First Name"),
    )
    family_name = CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name=_("Family Name"),
    )
    birth_date = DateField(
        blank=True,
        null=True,
        verbose_name=_("Birth Date"),
    )
    gender = CharField(
        max_length= 1,
        choices= Genders.choices,
        null=True,
        blank=True,
        verbose_name=_("Gender"),
    )
    language = ForeignKey(
        Language,
        on_delete=SET_NULL,
        null=True,
        blank=True,
        verbose_name= _("Language"),
    )
    location = ForeignKey(
        Location,
        null= True,
        blank= True,
        on_delete= CASCADE,
        related_name= "+",
        verbose_name= _("Location"),
    )
    address = ForeignKey(
        Address,
        null= True,
        blank= True,
        on_delete= CASCADE,
        related_name= "Profiles",
        verbose_name= _("Address"),
    )
    facebook_link = models.URLField(
        null=True,
        blank=True,
        verbose_name=_("FaceBook Link"),
    )

    @property
    def Full_Name(self) -> str:
        if self.first_name is None and self.family_name is None:
            return None
        return f"{str(self.first_name)} {str(self.family_name)}"
    
    @property
    def age(self) -> Age:
        born = self.birth_date
        calendar.setfirstweekday(calendar.SUNDAY)
        today = date.today()
        if today.month >= born.month:
            year = today.year
        else:
            year = today.year - 1
        age_years = year - born.year
        try:  # raised when birth day is February 29 and the current year is not a leap year
            age_days = (today - (born.replace(year=year))).days
        except ValueError:
            age_days = (today - (born.replace(year=year, day=born.day - 1))).days + 1
        month = born.month
        age_months = 0
        while age_days > calendar.monthrange(year, month)[1]:
            age_days = age_days - calendar.monthrange(year, month)[1]
            if month == 12:
                month = 1
                year += 1
            else:
                month += 1
            age_months += 1
        return Age(
            year = age_years,
            month = age_months,
            day = age_days,
        )
    
    @property
    def slug(self):
        return slugify(str(self.user.username))

    def __str__(self):
        return f"{self.user.username}"

    def __decode__(self):
        return f"{self.user.username}"

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")


class UserRestaurant(BaseModel):
    user = ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=CASCADE,
        related_name= "User_Restaurants",
        verbose_name= _("User"),
    )
    restaurant = ForeignKey(
        Restaurant,
        on_delete=CASCADE,
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
