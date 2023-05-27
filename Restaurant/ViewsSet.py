from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, filters
# from django_filters import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAdminUser 
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
import django_filters.rest_framework

from .models import Color, ColorStep, Gradient, Hospitality, Logo, Restaurant, RestaurantMeal, RestaurantMealSize, RestaurantMealImage, UserRestaurant
from .Serializer import (
    ColorSerializer,
    ColorStepSerializer,
    GradientSerializer,
    HospitalitySerializer,
    LogoSerializer,
    RestaurantMealImageSerializer,
    RestaurantMealSizeSerializer,
    RestaurantMealSerializer,
    RestaurantSerializer,
    UserRestaurantSerializer,
)


class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    filter_backends = (
        filters.OrderingFilter, # http://example.com/api/users?ordering=account,username
        filters.SearchFilter,  # http://example.com/api/users?search=russell
        django_filters.rest_framework.DjangoFilterBackend
    )
    ordering_fields = ('id', 'created_date', 'last_updated')
    filterset_fields = ['created_date', 'last_updated']
    search_fields = ['name', 'type']
    # This will be used as the default ordering
    ordering = ('-last_updated')


class HospitalityViewSet(ModelViewSet):
    queryset = Hospitality.objects.all()
    serializer_class = HospitalitySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    filter_backends = (
        filters.OrderingFilter, # http://example.com/api/users?ordering=account,username
        filters.SearchFilter,  # http://example.com/api/users?search=russell
        django_filters.rest_framework.DjangoFilterBackend
    )
    ordering_fields = ('id', 'created_date', 'last_updated')
    filterset_fields = ['created_date', 'last_updated']
    search_fields = ['name',]
    # This will be used as the default ordering
    ordering = ('-last_updated')
 

class RestaurantMealViewSet(ModelViewSet):
    queryset = RestaurantMeal.objects.all()
    serializer_class = RestaurantMealSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    filter_backends = (
        filters.OrderingFilter, # http://example.com/api/users?ordering=account,username
        filters.SearchFilter,  # http://example.com/api/users?search=russell
        django_filters.rest_framework.DjangoFilterBackend
    )
    ordering_fields = ('id', 'created_date', 'last_updated')
    filterset_fields = ['id', 'created_date', 'last_updated']
    search_fields = ['name', 'meal__name', 'restaurant__name']
    # This will be used as the default ordering
    ordering = ('-last_updated')


class RestaurantMealSizeViewSet(ModelViewSet):
    queryset = RestaurantMealSize.objects.all()
    serializer_class = RestaurantMealSizeSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    filter_backends = (
        filters.OrderingFilter, # http://example.com/api/users?ordering=account,username
        filters.SearchFilter,  # http://example.com/api/users?search=russell
        django_filters.rest_framework.DjangoFilterBackend
    )
    ordering_fields = ('id', 'created_date', 'last_updated')
    filterset_fields = ['id', 'created_date', 'last_updated', 'price']
    search_fields = ['restaurant_Meal__name', ]
    # This will be used as the default ordering
    ordering = ('-last_updated')


class RestaurantMealImageViewSet(ModelViewSet):
    queryset = RestaurantMealImage.objects.all()
    serializer_class = RestaurantMealImageSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    filter_backends = (
        filters.OrderingFilter, # http://example.com/api/users?ordering=account,username
        filters.SearchFilter,  # http://example.com/api/users?search=russell
        django_filters.rest_framework.DjangoFilterBackend
    )
    search_fields = ['restaurant_meal__name', ]


class ColorViewSet(ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]


class ColorStepViewSet(ModelViewSet):
    queryset = ColorStep.objects.all()
    serializer_class = ColorStepSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    filter_backends = (
        filters.OrderingFilter, # http://example.com/api/users?ordering=account,username
        filters.SearchFilter,  # http://example.com/api/users?search=russell
        django_filters.rest_framework.DjangoFilterBackend
    )
    search_fields = ['color__color', ]


class LogoViewSet(ModelViewSet):
    queryset = Logo.objects.all()
    serializer_class = LogoSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
   


class GradientViewSet(ModelViewSet):
    queryset = Gradient.objects.all()
    serializer_class = GradientSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]


class UserRestaurantViewSet(ModelViewSet):
    queryset = UserRestaurant.objects.all()
    serializer_class = UserRestaurantSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    filter_backends = (
        filters.OrderingFilter, # http://example.com/api/users?ordering=account,username
        filters.SearchFilter,  # http://example.com/api/users?search=russell
        django_filters.rest_framework.DjangoFilterBackend
    )
    ordering_fields = ('id', 'created_date', 'last_updated', 'likes', 'review')
    filterset_fields = ['created_date', 'last_updated']
    search_fields = ['user__id', 'restaurant__name', 'is_favorite', 'is_favorite', 'likes']
    # This will be used as the default ordering
    ordering = ('-last_updated')

    def get_queryset(self):
        return UserRestaurant.objects.all().filter(user=self.request.user)
