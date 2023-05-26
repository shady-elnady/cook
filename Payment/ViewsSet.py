from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser 
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
import django_filters.rest_framework

from .models import Currency, PaymentMethod
from .Serializer import CurrencySerializer, PaymentMethodSerializer


class CurrencyViewSet(ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    filter_backends = (
        filters.OrderingFilter, # http://example.com/api/users?ordering=account,username
        filters.SearchFilter,  # http://example.com/api/users?search=russell
        django_filters.rest_framework.DjangoFilterBackend
    )
    ordering_fields = ('id', 'created_date', 'last_updated')
    filterset_fields = ['id', 'created_date', 'last_updated']
    search_fields = ['name', 'native', 'code', 'symbol']
    # This will be used as the default ordering
    ordering = ('-last_updated')


class PaymentMethodViewSet(ModelViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    filter_backends = (
        filters.OrderingFilter, # http://example.com/api/users?ordering=account,username
        filters.SearchFilter,  # http://example.com/api/users?search=russell
        django_filters.rest_framework.DjangoFilterBackend
    )
    ordering_fields = ('id', 'created_date', 'last_updated')
    filterset_fields = ['id', 'created_date', 'last_updated']
    search_fields = ['name', ]
    # This will be used as the default ordering
    ordering = ('-last_updated')