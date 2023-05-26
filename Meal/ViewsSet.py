from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser 
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
import django_filters.rest_framework

from .models import Meal
from .Serializer import MealSerializer




class MealViewSet(ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    filter_backends = (
        filters.OrderingFilter, # http://example.com/api/users?ordering=account,username
        filters.SearchFilter,  # http://example.com/api/users?search=russell
        django_filters.rest_framework.DjangoFilterBackend
    )
    ordering_fields = ('id', 'created_date', 'last_updated')
    filterset_fields = ['id', 'created_date', 'last_updated']
    search_fields = ['name', 'category__name']
    # This will be used as the default ordering
    ordering = ('-last_updated')