from rest_framework.serializers import  HyperlinkedModelSerializer
from Language.Serializer import LanguageSerializer
from Location.Serializer import LocationSerializer
from Payment.Serializer import CurrencySerializer

from Restaurant.Serializer import RestaurantSerializer

from .models import  Address, Street, Area, City, Governorate, Country



class CountrySerializer(HyperlinkedModelSerializer):
    currency= CurrencySerializer(many= False)
    language = LanguageSerializer(many= False)

    class Meta:
        model = Country
        fields = [
            "url",
            "id",
            "name",
            "native",
            "continent",
            "capital",
            "flag_emoji",
            "currency",
            "language",
            "tel_code",
            "time_zones",
            "created_date",
            "last_updated",
            "slug",
        ]
 


class GovernorateSerializer(HyperlinkedModelSerializer):
    country = CountrySerializer(many= False)

    class Meta:
        model = Governorate
        fields = [
            "url",
            "id",
            "name",
            "native",
            "country",
            "tel_code",
            "created_date",
            "last_updated",
            "slug",
        ]
 


class CitySerializer(HyperlinkedModelSerializer):
    country = CountrySerializer(many= False)
    governorate = GovernorateSerializer(many= False)

    class Meta:
        model = City
        fields = [
            "url",
            "id",
            "name",
            "native",
            "country",
            "governorate",
            "created_date",
            "last_updated",
            "slug",
        ]
 


class AreaSerializer(HyperlinkedModelSerializer):
    city = CitySerializer(many= False)

    class Meta:
        model = Area
        fields = [
            "url",
            "id",
            "name",
            "native",
            "city",
            "postal_code",
            "area_category",
            "created_date",
            "last_updated",
            "slug",
        ]
 


class StreetSerializer(HyperlinkedModelSerializer):
    area = RestaurantSerializer(many= False)

    class Meta:
        model = Street
        fields = [
            "url",
            "id",
            "name",
            "native",
            "area",
            "created_date",
            "last_updated",
            "slug",
        ]
 

class AddressSerializer(HyperlinkedModelSerializer):
    street = StreetSerializer(many= False)

    class Meta:
        model = Address
        fields = [
            "url",
            "id",
            "name",
            "native",
            "street",
            "lat",
            "lang",
            "created_date",
            "last_updated",
            "slug",
        ]
 
