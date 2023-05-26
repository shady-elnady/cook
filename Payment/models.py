from django.db import models
from django.utils.translation import gettext_lazy as _

from Utils.models import BaseModelImage, BaseModelName, BaseModelNative

# Create your models here.



class PaymentMethod(BaseModelName, BaseModelImage):
  
    class Meta:
        verbose_name= _("Payment Method")
        verbose_name_plural= _("Payment Methods")


class Currency(BaseModelNative):
    code= models.CharField(
        max_length=3,
        unique= True,
        verbose_name=_("Code"),
    )
    symbol= models.CharField(
        max_length= 3,
        unique= True,
        verbose_name= _("Symbol"),
    )
  
    class Meta:
        verbose_name= _("Currency")
        verbose_name_plural= _("Currencies")
