from rest_framework.serializers import HyperlinkedModelSerializer 

from .models import Notification
from User.Serializer import UserSerializer
# Serializers define the API representation.


class NotificationSerializer(HyperlinkedModelSerializer):
    user = UserSerializer(many= False)
    class Meta:
        model = Notification
        fields = [
            "url",
            "id",
            "user",
            "meassage",
            "created_date",
            "last_updated",
            "slug",
        ]

