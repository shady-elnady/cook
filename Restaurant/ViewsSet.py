from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, filters
# from django_filters import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAdminUser 
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication

from .models import Color, ColorStep, Gradient, Logo, Restaurant, RestaurantMeal, RestaurantMealSize, RestaurantMealImage
from .Serializer import (
    ColorSerializer,
    ColorStepSerializer,
    GradientSerializer,
    LogoSerializer,
    RestaurantMealImageSerializer,
    RestaurantMealSizeSerializer,
    RestaurantMealSerializer,
    RestaurantSerializer,
)


class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
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

    # # def get_queryset(self):
    # #     is_best = self.kwargs['is_best']
    # #     queryset = Restaurant.objects.all()
    # #     if is_best:
    # #         return queryset.order_by("")
    # #     return queryset
 

class RestaurantMealViewSet(ModelViewSet):
    queryset = RestaurantMeal.objects.all()
    serializer_class = RestaurantMealSerializer
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


class RestaurantMealSizeViewSet(ModelViewSet):
    queryset = RestaurantMealSize.objects.all()
    serializer_class = RestaurantMealSizeSerializer
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


class RestaurantMealImageViewSet(ModelViewSet):
    queryset = RestaurantMealImage.objects.all()
    serializer_class = RestaurantMealImageSerializer
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


class ColorViewSet(ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
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


class ColorStepViewSet(ModelViewSet):
    queryset = ColorStep.objects.all()
    serializer_class = ColorStepSerializer
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


class LogoViewSet(ModelViewSet):
    queryset = Logo.objects.all()
    serializer_class = LogoSerializer
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


class GradientViewSet(ModelViewSet):
    queryset = Gradient.objects.all()
    serializer_class = GradientSerializer
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

 