from rest_framework.serializers import HyperlinkedModelSerializer 

from .models import Meal
from Category.Serializer import CategorySerializer

# Serializers define the API representation.



class MealSerializer(HyperlinkedModelSerializer):
    category = CategorySerializer(many= False)

    class Meta:
        model = Meal
        fields = [
            "url",
            "id",
            "name",
            "category",
            "created_date",
            "last_updated",
            "slug",
        ]
