from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser 
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication

from .models import Language
from .Serializer import LanguageSerializer


class LanguageViewSet(ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]