from rest_framework.serializers import HyperlinkedModelSerializer

from Address.Serializer import AddressSerializer

from .models import Order, OrderMeal, OrderRateDriver, OrderRateRestaurant
from Restaurant.Serializer import RestaurantMealSizeSerializer, RestaurantSerializer
from Driver.Serializer import DriverSerializer
from Payment.Serializer import PaymentMethodSerializer 

# Serializers define the API representation.


class OrderMealSerializer(HyperlinkedModelSerializer):
    meal = RestaurantMealSizeSerializer(many= False)

    class Meta:
        model = OrderMeal
        fields = [
            "url",
            "id",
            "order",
            "meal",
            "quantity",
            "Total_meal_price",
            "created_date",
            "last_updated",
            "slug",
        ]


class OrderRateDriverSerializer(HyperlinkedModelSerializer):
    driver = DriverSerializer(many= False)

    class Meta:
        model = OrderRateDriver
        fields = [
            "url",
            "id",
            "order",
            "driver",
            "reviews",
            "comment",
            "is_good_service",
            "is_on_time",
            "is_clean",
            "is_carefull",
            "is_work_hard",
            "is_polite",
            "created_date",
            "last_updated",
            "slug",
        ]


class OrderRateRestaurantSerializer(HyperlinkedModelSerializer):
    restaurant = RestaurantSerializer(many= False)

    class Meta:
        model = OrderRateRestaurant
        fields = [
            "url",
            "id",
            "order",
            "restaurant",
            "reviews",
            "comment",
            "is_good_package",
            "is_clean",
            "is_pair_price",
            "created_date",
            "last_updated",
            "slug",
        ]



class OrderSerializer(HyperlinkedModelSerializer):
    Order_Meals = OrderMealSerializer(many= True)
    Order_Rate_Driver = OrderRateDriverSerializer(many = False)
    Order_Rate_Restaurant = OrderRateRestaurantSerializer(many = False)
    payment_method = PaymentMethodSerializer(many = False)
    address = AddressSerializer(many= False)
    
    class Meta:
        model = Order
        fields = [
            "url",
            "id",
            "customer",
            "payment_method",
            "status",
            "is_paid",
            "Order_Meals",
            "address",
            "Order_Rate_Driver",
            "Order_Rate_Restaurant",
            "Total_order_price",
            "created_date",
            "last_updated",
            "slug",
        ]
