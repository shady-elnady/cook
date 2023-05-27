import base64
from datetime import datetime
from django.contrib.auth import authenticate

from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status, filters
from django.core.exceptions import ObjectDoesNotExist
import django_filters.rest_framework

from .models import  Address, Street, Area, City, Governorate, Country
from .Serializer import (
    AddressSerializer, AreaSerializer, CitySerializer,
    CountrySerializer, GovernorateSerializer, StreetSerializer,
)

# import pyotp

class AddressViewSet(ModelViewSet):
    """
    API endpoint that allows Addresss to be viewed or edited.
    """
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    filter_backends = (
        filters.OrderingFilter, # http://example.com/api/users?ordering=account,username
        filters.SearchFilter,  # http://example.com/api/users?search=russell
        django_filters.rest_framework.DjangoFilterBackend
    )
    ordering_fields = ('id', 'created_date', 'last_updated')
    filterset_fields = ['id', 'created_date', 'last_updated']
    search_fields = ['name', 'native']
    # This will be used as the default ordering
    ordering = ('-last_updated')


"""
    ?page=1&size=15&sorters[0]

    http://example.com/api/users?ordering=account,username

"""
class StreetViewSet(ModelViewSet):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (
        filters.OrderingFilter,
    )



class AreaViewSet(ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (
        filters.OrderingFilter,
    )
    # Explicitly specify which fields the API may be ordered against
    ordering_fields = ('id', 'created_date', 'name')
    # This will be used as the default ordering
    ordering = ('last_updated')


class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (
        filters.OrderingFilter,
        # DjangoFilterBackend,
    )
     # Explicitly specify which fields the API may be ordered against
    ordering_fields = ('id', 'created_date', 'name')
    # This will be used as the default ordering
    ordering = ('last_updated')
    

class GovernorateViewSet(ModelViewSet):
    queryset = Governorate.objects.all()
    serializer_class = GovernorateSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (
        filters.OrderingFilter,
        # DjangoFilterBackend,
    )
     # Explicitly specify which fields the API may be ordered against
    ordering_fields = ('id', 'created_date', 'name')
    # This will be used as the default ordering
    ordering = ('last_updated')



class CountryViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (
        filters.OrderingFilter, # http://example.com/api/users?ordering=account,username
        filters.SearchFilter,  # http://example.com/api/users?search=russell
        django_filters.rest_framework.DjangoFilterBackend
    )
    ordering_fields = ('id', 'created_date', 'last_updated')
    filterset_fields = ['id', 'created_date', 'last_updated']
    search_fields = ['restaurant_Meal__name', ]
    # This will be used as the default ordering
