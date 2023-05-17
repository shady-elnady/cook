from rest_framework.serializers import  HyperlinkedModelSerializer
from Location.Serializer import LocationSerializer

from Restaurant.Serializer import RestaurantSerializer

from .models import User, Profile, UserRestaurant
from Language.Serializer import LanguageSerializer



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
 

class UserSerializer(HyperlinkedModelSerializer):
    User_Restaurants = UserRestaurantSerializer(many= True)

    class Meta:
        model = User
        fields = [
            "url",
            "username",
            "email",
            "User_Restaurants",
            "slug",
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
 

class ProfileSerializer(HyperlinkedModelSerializer):
    user = UserSerializer(many= False)
    language = LanguageSerializer(many= False)
    location = LocationSerializer(many= False)

    class Meta:
        model = Profile
        fields = [
            "url",
            "id",
            "user",
            "image",
            "phone_number",
            "first_name",
            "family_name",
            "birth_date",
            "gender",
            "language",
            "full_name",
            "age",
            "location",
            "created_date",
            "last_updated",
            "slug",
        ]