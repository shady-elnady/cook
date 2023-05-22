import base64
from datetime import datetime
from django.contrib.auth import authenticate

from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist

from .models import  Address, Street, Area, City, Governorate, Country
from .Serializer import AddressSerializer, AreaSerializer, CitySerializer, CountrySerializer, GovernorateSerializer, StreetSerializer

# import pyotp


class AddressViewSet(ModelViewSet):
    """
    API endpoint that allows Addresss to be viewed or edited.
    """
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_queryset(self):
        return Address.objects.all().filter(user=self.request.user)


class StreetViewSet(ModelViewSet):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Street.objects.all().filter(user=self.request.user)


class AreaViewSet(ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Area.objects.all().filter(user=self.request.user)


class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return City.objects.all().filter(user=self.request.user)


class GovernorateViewSet(ModelViewSet):
    queryset = Governorate.objects.all()
    serializer_class = GovernorateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Governorate.objects.all().filter(user=self.request.user)


class CountryViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Country.objects.all().filter(user=self.request.user)

