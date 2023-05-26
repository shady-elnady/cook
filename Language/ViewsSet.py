from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser 
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework import filters
import django_filters.rest_framework

from .models import Language
from .Serializer import LanguageSerializer


class LanguageViewSet(ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    filter_backends = (
        filters.OrderingFilter, # http://example.com/api/users?ordering=account,username
        filters.SearchFilter,  # http://example.com/api/users?search=russell
        django_filters.rest_framework.DjangoFilterBackend
    )
    ordering_fields = ('id', 'created_date', 'last_updated')
    filterset_fields = ['id', 'created_date', 'last_updated']
    search_fields = ['name', 'native', 'symbol', 'rtl']
    # This will be used as the default ordering
    ordering = ('-last_updated')