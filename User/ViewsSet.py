import base64
from datetime import datetime
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated, IsAdminUser 
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
import django_filters.rest_framework

from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status, filters
from django.core.exceptions import ObjectDoesNotExist

from .models import User, Profile
from .Serializer import (
    UserSerializer,
    ProfileSerializer,
)
# import pyotp



class UserViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]

    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response(
                {
                    "token": user.auth_token.key,
                },
            )
        else:
            return Response(
                {
                    "error": "Wrong Credentials",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


class MyProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]

    def get_queryset(self):
        return Profile.objects.all().filter(user=self.request.user)


