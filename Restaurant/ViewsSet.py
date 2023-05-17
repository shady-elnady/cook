from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import IsAuthenticated, IsAdminUser 

from .models import (
    Restaurant, RestaurantMeal,
    RestaurantMealSize, RestaurantMealImage,
)
from .Serializer import (
    RestaurantMealImageSerializer,
    RestaurantMealSizeSerializer,
    RestaurantMealSerializer,
    RestaurantSerializer,
)



class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser]

 

class RestaurantMealViewSet(ModelViewSet):
    queryset = RestaurantMeal.objects.all()
    serializer_class = RestaurantMealSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser]

 

class RestaurantMealSizeViewSet(ModelViewSet):
    queryset = RestaurantMealSize.objects.all()
    serializer_class = RestaurantMealSizeSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser]

 

class RestaurantMealImageViewSet(ModelViewSet):
    queryset = RestaurantMealImage.objects.all()
    serializer_class = RestaurantMealImageSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser]

 