from rest_framework.serializers import HyperlinkedModelSerializer 

from .models import Language
# Serializers define the API representation.


class LanguageSerializer(HyperlinkedModelSerializer):
    
    class Meta:
        model = Language
        fields = [
            "url",
            "id",
            "name",
            "native",
            "symbol",
            "emoji",
            "rtl",
            "created_date",
            "last_updated",
            "slug",
        ]
