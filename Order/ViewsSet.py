from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import IsAuthenticated, IsAdminUser 

from .models import Order, OrderMeal, OrderRateDriver, OrderRateRestaurant
from .Serializer import OrderSerializer, OrderMealSerializer, OrderRateDriverSerializer, OrderRateRestaurantSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser]


class OrderMealViewSet(ModelViewSet):
    queryset = OrderMeal.objects.all()
    serializer_class = OrderMealSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser]


class OrderRateDriverViewSet(ModelViewSet):
    queryset = OrderRateDriver.objects.all()
    serializer_class = OrderRateDriverSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser]


class OrderRateRestaurantViewSet(ModelViewSet):
    queryset = OrderRateRestaurant.objects.all()
    serializer_class = OrderRateRestaurantSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser]

 