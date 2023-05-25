from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser 
from rest_framework.views import APIView

from rest_framework.response import Response
from django.contrib.auth import get_user_model

from .Utils import otp_generator
from django.contrib.auth import login
from rest_framework import permissions, generics, status, serializers
import requests
from rest_framework.authtoken.models import Token

from .TwilioMessageHandler import TwilioMessageHandler
from .Serializer import  RegisterSerializer

User = get_user_model()

# Create your views here.


class RegisterViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

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
    

def send_otp(mobile, otp_key):
    """
    This is an helper function to send otp to session stored mobiles or 
    passed mobile number as argument.    """
    if mobile:
        mobile = str(mobile)
        # otp_key = str(otp_generator())
        link = f'https://2factor.in/API/R1/?module=TRANS_SMS&apikey=7c59cf94-d129-11ec-9c12-0200cd936042&to={mobile}&from=MMBook&templatename=mymedbook&var1={otp_key}&var2={otp_key}'
        result = requests.get(link, verify=False)
        print(result)
        return otp_key
    else:
        return False

