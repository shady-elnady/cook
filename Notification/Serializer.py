from rest_framework.serializers import HyperlinkedModelSerializer 

from .models import Notification
# Serializers define the API representation.


class NotificationSerializer(HyperlinkedModelSerializer):
    
    class Meta:
        model = Notification
        fields = [
            "url",
            "id",
            "created_date",
            "last_updated",
            "slug",
        ]

