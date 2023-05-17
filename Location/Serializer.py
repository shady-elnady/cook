from rest_framework.serializers import HyperlinkedModelSerializer 

from .models import Location
# Serializers define the API representation.


class LocationSerializer(HyperlinkedModelSerializer):
    
    class Meta:
        model = Location
        fields = [
            "url",
            "address",
            "lat",
            "lang",
        ]
