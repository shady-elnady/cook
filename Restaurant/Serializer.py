from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Color, ColorStep, Gradient, Hospitality, Logo, Restaurant, RestaurantMeal, RestaurantMealSize, RestaurantMealImage, UserRestaurant
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
            "id",
            "color",
            "step",
        ]


class GradientSerializer(HyperlinkedModelSerializer):
    Colors_Steps = ColorStepSerializer(many= True)

    class Meta:
        model = Gradient
        fields = [
            "url",
            "gradient_type",
            "begin",
            "end",
            "Colors_Steps",
        ]


class LogoSerializer(HyperlinkedModelSerializer):
    gradient = GradientSerializer(many= False)

    class Meta:
        model = Logo
        fields = [
            "url",
            "id",
            "Restaurant",
            "gradient",
            "image",
        ]


class RestaurantMealImageSerializer(HyperlinkedModelSerializer):
    
    class Meta:
        model = RestaurantMealImage
        fields = [
            "url",
            "restaurant_meal",
            "image",
            "slug",
        ]


class HospitalitySerializer(HyperlinkedModelSerializer):
    
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
    Images = RestaurantMealImageSerializer(many= True)
    
    class Meta:
        model = RestaurantMeal
        fields = [
            "url",
            "id",
            "name",
            "restaurant",
            "meal",
            "orders_count",
            "Restaurant_Meals_Sizes",
            # "primary_image",
            "Images",
            "created_date",
            "last_updated",
            "slug",
        ]


class RestaurantSerializer(HyperlinkedModelSerializer):
    Restaurant_Meals = RestaurantMealSerializer(many=True)
    categories = CategorySerializer(many= True)
    address = AddressSerializer(many= False)
    logo= LogoSerializer(many= False)
    hospitalities= HospitalitySerializer(many= True)

    class Meta:
        model = Restaurant
        fields = [
            "url",
            "id",
            "name",
            "free_shipping",
            "type",
            "open_time",
            "close_time",
            "address",
            "hospitalities",
            "categories",
            # "is_Opened",
            # "users_choiced_count", ##
            # "Likes",
            # "Reviews",
            "logo",
            "Restaurant_Meals",
            "created_date",
            "last_updated",
            "slug",
        ]



class UserRestaurantSerializer(HyperlinkedModelSerializer):
    restaurant = RestaurantSerializer(many= False)

    class Meta:
        model = UserRestaurant
        fields = [
            "url",
            "id",
            "user",
            "restaurant",
            "is_favorite",
            "comment",
            "review",
            "likes",
            "slug",
        ]
 
