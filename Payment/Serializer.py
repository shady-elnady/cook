from rest_framework.serializers import HyperlinkedModelSerializer 

from .models import Currency, PaymentMethod
# Serializers define the API representation.


class CurrencySerializer(HyperlinkedModelSerializer):
    
    class Meta:
        model = Currency
        fields = [
            "url",
            "id",
            "name",
            "native",
            "code",
            "symbol",
            "created_date",
            "last_updated",
            "slug",
        ]


class PaymentMethodSerializer(HyperlinkedModelSerializer):
    
    class Meta:
        model = PaymentMethod
        fields = [
            "url",
            "id",
            "name",
            "image",
            "created_date",
            "last_updated",
            "slug",
        ]
