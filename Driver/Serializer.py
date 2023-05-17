from rest_framework.serializers import HyperlinkedModelSerializer 

from .models import Driver
# Serializers define the API representation.


class DriverSerializer(HyperlinkedModelSerializer):
    
    class Meta:
        model = Driver
        fields = [
            "url",
            "id",
            "name",
            "image",
            "phone_number",
            "slug",
        ]

