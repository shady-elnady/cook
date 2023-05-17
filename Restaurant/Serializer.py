from rest_framework.serializers import HyperlinkedModelSerializer

from Location.Serializer import LocationSerializer


from .models import Restaurant, RestaurantMeal, RestaurantMealSize, RestaurantMealImage
from Meal.Serializer import MealSerializer
from Category.Serializer import CategorySerializer
from Payment.Serializer import CurrencySerializer 

# Serializers define the API representation.




class RestaurantMealImageSerializer(HyperlinkedModelSerializer):
    
    class Meta:
        model = RestaurantMealImage
        fields = [
            "url",
            "Restaurant_Meal",
            "image",
            "slug",
        ]


class RestaurantMealSizeSerializer(HyperlinkedModelSerializer):
    currency = CurrencySerializer(many= False)
    
    class Meta:
        model = RestaurantMealSize
        fields = [
            "url",
            "id",
            "restaurant_Meal",
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
            "restaurant",
            "meal",
            "Restaurant_Meals_Sizes",
            "images",
            "slug",
        ]


class RestaurantSerializer(HyperlinkedModelSerializer):
    Restaurant_Meals = MealSerializer(many=True)
    Categories = CategorySerializer(many= True)
    location = LocationSerializer(many= False)
    
    class Meta:
        model = Restaurant
        fields = [
            "url",
            "id",
            "name",
            "is_best",
            "free_shipping",
            "Restaurant_Meals",
            "type",
            "open_time",
            "close_time",
            "lat",
            "lang",
            "reviews",
            "Categories",
            "image",
            "location",
            "created_date",
            "last_updated",
            "slug",
        ]
