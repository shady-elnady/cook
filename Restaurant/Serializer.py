from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Color, ColorStep, Gradient, Hospitality, Logo, Restaurant, RestaurantMeal, RestaurantMealSize, RestaurantMealImage
from Address.Serializer import AddressSerializer
from Meal.Serializer import MealSerializer
from Category.Serializer import CategorySerializer
from Payment.Serializer import CurrencySerializer 

# Serializers define the API representation.


class ColorSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Color
        fields = [
            "url",
            "color",
        ]


class ColorStepSerializer(HyperlinkedModelSerializer):
    color = ColorSerializer(many= False)

    class Meta:
        model = ColorStep
        fields = [
            "url",
            "color",
            "step",
        ]


class GradientSerializer(HyperlinkedModelSerializer):
    Colors_steps = ColorStepSerializer(many= True)

    class Meta:
        model = Gradient
        fields = [
            "url",
            "gradient_type",
            "begin",
            "end",
            "colors_steps",
            "image",
        ]


class LogoSerializer(HyperlinkedModelSerializer):
    color = ColorSerializer(many= False)
    gradient = GradientSerializer(many= False)

    class Meta:
        model = Logo
        fields = [
            "url",
            "restaurant",
            "gradient",
            "image",
        ]


class RestaurantMealImageSerializer(HyperlinkedModelSerializer):
    
    class Meta:
        model = RestaurantMealImage
        fields = [
            "url",
            "Restaurant_Meal",
            "image",
            "slug",
        ]


class HospitalitySerializer(HyperlinkedModelSerializer):
    currency = CurrencySerializer(many= False)
    
    class Meta:
        model = Hospitality
        fields = [
            "url",
            "id",
            "name",
            "created_date",
            "last_updated",
            "slug",
        ]

class RestaurantMealSizeSerializer(HyperlinkedModelSerializer):
    currency = CurrencySerializer(many= False)
    
    class Meta:
        model = RestaurantMealSize
        fields = [
            "url",
            "id",
            "restaurant_meal",
            "size",
            "price",
            "currency",
            "created_date",
            "last_updated",
            "slug",
        ]


class RestaurantMealSerializer(HyperlinkedModelSerializer):
    meal = MealSerializer(many= False)
    Restaurant_Meals_Sizes = RestaurantMealSizeSerializer(many= True)
    images = RestaurantMealImageSerializer(many= True)
    
    class Meta:
        model = RestaurantMeal
        fields = [
            "url",
            "id",
            "name",
            "restaurant",
            "meal",
            "Restaurant_Meals_Sizes",
            "orders_count",
            "primary_image",
            "images",
            "created_date",
            "last_updated",
            "slug",
        ]


class RestaurantSerializer(HyperlinkedModelSerializer):
    Restaurant_Meals = MealSerializer(many=True)
    Categories = CategorySerializer(many= True)
    address = AddressSerializer(many= False)
    Logo= LogoSerializer(many= False)

    class Meta:
        model = Restaurant
        fields = [
            "url",
            "id",
            "name",
            "free_shipping",
            "Restaurant_Meals",
            "type",
            "open_time",
            "close_time",
            "lat",
            "lang",
            "reviews",
            "Categories",
            "Logo",
            "address",
            "Reviews",
            "Likes",
            "is_Opened",
            "created_date",
            "last_updated",
            "users_choiced_count", ##
            "slug",
        ]
