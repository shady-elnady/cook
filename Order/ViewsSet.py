from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser 
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
import django_filters.rest_framework

from .models import Order, OrderMeal, OrderRateDriver, OrderRateRestaurant
from .Serializer import OrderSerializer, OrderMealSerializer, OrderRateDriverSerializer, OrderRateRestaurantSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    filter_backends = (
        filters.OrderingFilter, # http://example.com/api/users?ordering=account,username
        filters.SearchFilter,  # http://example.com/api/users?search=russell
        django_filters.rest_framework.DjangoFilterBackend
    )
    ordering_fields = ('id', 'created_date', 'last_updated')
    filterset_fields = ['id', 'created_date', 'last_updated']
    search_fields = ['customer__id', 'payment_method__id', 'address__id']
    # This will be used as the default ordering
    ordering = ('-last_updated')



class OrderMealViewSet(ModelViewSet):
    queryset = OrderMeal.objects.all()
    serializer_class = OrderMealSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    filter_backends = (
        filters.OrderingFilter, # http://example.com/api/users?ordering=account,username
        filters.SearchFilter,  # http://example.com/api/users?search=russell
        django_filters.rest_framework.DjangoFilterBackend
    )
    ordering_fields = ('id', 'created_date', 'last_updated')
    filterset_fields = ['id', 'created_date', 'last_updated']
    search_fields = ['order__id', 'meal__id']
    # This will be used as the default ordering
    ordering = ('-last_updated')



class OrderRateDriverViewSet(ModelViewSet):
    queryset = OrderRateDriver.objects.all()
    serializer_class = OrderRateDriverSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    filter_backends = (
        filters.OrderingFilter, # http://example.com/api/users?ordering=account,username
        filters.SearchFilter,  # http://example.com/api/users?search=russell
        django_filters.rest_framework.DjangoFilterBackend
    )
    ordering_fields = ('id', 'created_date', 'last_updated')
    filterset_fields = ['id', 'created_date', 'last_updated']
    search_fields = ['order__id', 'driver__id']
    # This will be used as the default ordering
    ordering = ('-last_updated')



class OrderRateRestaurantViewSet(ModelViewSet):
    queryset = OrderRateRestaurant.objects.all()
    serializer_class = OrderRateRestaurantSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    filter_backends = (
        filters.OrderingFilter, # http://example.com/api/users?ordering=account,username
        filters.SearchFilter,  # http://example.com/api/users?search=russell
        django_filters.rest_framework.DjangoFilterBackend
    )
    ordering_fields = ('id', 'created_date', 'last_updated')
    filterset_fields = ['id', 'created_date', 'last_updated']
    search_fields = ['order__id', 'restaurant__id']
    # This will be used as the default ordering
    ordering = ('-last_updated')


 