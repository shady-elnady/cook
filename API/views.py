from django.shortcuts import render
from django.contrib.auth import login
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics, status


from .Serializer import LoginSerializer, RegisterSerializer
from User.models import User
from User.Serializer import UserSerializer

# Create your views here.

# Class based view to Get User Details using Token Authentication

class UserDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  def get(self,request,*args,**kwargs):
    user = User.objects.get(id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data)



#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer



class LoginView(APIView):
  # This view should be accessible also for unauthenticated users.
  permission_classes = (AllowAny,)

  def post(self, request, format=None):
    serializer = LoginSerializer(
      data=self.request.data,
      context={ 'request': self.request },
    )
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    login(request, user)
    return Response(None, status=status.HTTP_202_ACCEPTED)