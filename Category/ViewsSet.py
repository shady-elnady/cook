from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser 
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework import filters
# from django_filters import DjangoFilterBackend

from .models import Category
from .Serializer import CategorySerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    # filter_backends = [filters.OrderingFilter]
    filter_backends = (
        filters.OrderingFilter,
        # DjangoFilterBackend,
    )
     # Explicitly specify which fields the API may be ordered against
    ordering_fields = ('id', 'created_date', 'name')
    # This will be used as the default ordering
    ordering = ('last_updated')

    # ordering_filter = filters.OrderingFilter()

    # def filter_queryset(self, queryset):
    #     queryset = super(YOUR_VIEW_SET, self).filter_queryset(queryset)
    #     return self.ordering_filter.filter_queryset(self.request, queryset, self)


"""
 http://example.com/api/users?ordering=username

"""