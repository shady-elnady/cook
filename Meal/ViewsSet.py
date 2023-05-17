from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import IsAuthenticated, IsAdminUser 

from .models import Meal
from .Serializer import MealSerializer




class MealViewSet(ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser]

 
