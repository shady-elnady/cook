from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser 
from rest_framework.views import APIView

from rest_framework.response import Response
from django.contrib.auth import get_user_model

from django.contrib.auth import login
from rest_framework import permissions, generics, status, serializers
import requests
from rest_framework.authtoken.models import Token
# from django.views.decorators.csrf import csrf_exempt

from .TwilioMessageHandler import TwilioMessageHandler
from .Serializer import  ChangePasswordSerializer, RegisterSerializer

User = get_user_model()

# Create your views here.


class RegisterViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    # @csrf_exempt
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {
                'data': serializer.data,
                'success': True,
                'message': 'User created successfully. You Can LogIN now',
                'status': status.HTTP_201_CREATED,          
            },
            status= status.HTTP_201_CREATED,
        )

    def get_queryset(self):
        raise serializers.ValidationError(
                'This URL To Register '
            )
