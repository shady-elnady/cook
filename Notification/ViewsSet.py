from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser 
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from .models import Notification
from .Serializer import NotificationSerializer


class NotificationViewSet(ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    filter_backends = (
        filters.OrderingFilter,
        # DjangoFilterBackend,
    )
     # Explicitly specify which fields the API may be ordered against
    ordering_fields = ('id', 'created_date', 'name')
    # This will be used as the default ordering
    ordering = ('last_updated')