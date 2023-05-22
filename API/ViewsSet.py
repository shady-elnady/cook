from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser 

from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .Utils import otp_generator
from knox.models import AuthToken
from django.contrib.auth import login
from rest_framework import permissions, generics, status
import requests
from rest_framework import serializers

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

    

def send_otp(mobile):
    """
    This is an helper function to send otp to session stored mobiles or 
    passed mobile number as argument.    """
    if mobile:
        key = otp_generator()
        mobile = str(mobile)
        otp_key = str(key)
        link = f'https://2factor.in/API/R1/?module=TRANS_SMS&apikey=7c59cf94-d129-11ec-9c12-0200cd936042&to={mobile}&from=MMBook&templatename=mymedbook&var1={otp_key}&var2={otp_key}'
        result = requests.get(link, verify=False)
        print(result)
        return otp_key
    else:
        return False


class MobileSendOTP(APIView):
    def post(self, request, *agrs, **kwargs):
        try:
            mobile_number = request.data.get('mobile')
            user_id = request.data.get('user_id')
            if mobile_number and user_id:
                mobile = str(mobile_number)
                user = User.objects.filter(id__iexact=user_id)
                if user.exists():
                    user_data = user.first()
                    old_otp = user_data.otp
                    new_otp = send_otp(mobile)
                    user_data.mobile = mobile
                    user_data.otp = new_otp
                    if old_otp:
                        user_data.otp_enabled = False
                        user_data.is_verified = False
                        user_data.save()
                        return Response(
                            {
                                'success': True,
                                'message': 'OTP sent successfully, get it',
                                'status': status.HTTP_200_OK,
                            },
                            status= status.HTTP_200_OK,
                        )
                    else:
                        user_data.save()
                        return Response(
                            {
                                "scucess": True,
                                'message': 'OTP sent successfully, get it',
                                'status': status.HTTP_200_OK,
                            },
                            status= status.HTTP_200_OK,
                        )
                else:
                    return Response(
                        {
                            'success': False,
                            'message': 'User not found ! please register',
                            'status': status.HTTP_404_NOT_FOUND,
                        },
                        status= status.HTTP_400_BAD_REQUEST,
                    )
            else:
                return Response(
                    {
                        'success': False,
                        'message': 'Mobile number and User ID is required',
                        'status': status.HTTP_400_BAD_REQUEST
                    },
                    status= status.HTTP_400_BAD_REQUEST,
                )
        except Exception as e:
            return Response(
                {
                    'success': False,
                    'message': str(e),
                    'status': status.HTTP_400_BAD_REQUEST,
                },
                status= status.HTTP_400_BAD_REQUEST,
            )


# verify otp
class VerifymobileOTPView(APIView):
    def post(self, request, format=None):
        try:
            otp = request.data.get('otp')
            user_id = request.data.get('user_id')
            print(otp, user_id)
            if otp and user_id:
                user = User.objects.filter(id__iexact=user_id)
                if user.exists():
                    user = user.first()
                    login(request, user)
                    if user.otp == otp:
                        user.otp_enabled = True
                        user.is_verified = True
                        user.save()
                        return Response(
                            {
                                'status': True,
                                'message': 'Login Successfully',
                                'token': AuthToken.objects.create(user)[1],
                                'response': {
                                    'id': user.id,
                                    'username': user.username,
                                    'email': user.email,
                                    'mobile': user.mobile,
                                    'otp': user.otp,
                                    'Profile': user.Profile,
                                },
                            },
                            status=status.HTTP_200_OK,
                        )
                    else:
                        return Response(
                            {
                            'success': False,
                            'message': 'OTP does not match'
                            }, 
                            status=status.HTTP_400_BAD_REQUEST
                        )
                else:
                    return Response(
                        {
                        'success': False,
                        'message': 'User does not exist'
                        }, 
                        status=status.HTTP_403_FORBIDDEN
                    )
            else:
                return Response(
                    {
                    'success': False,
                    'message': 'mobile or OTP is missing'
                    }, 
                    status=status.HTTP_403_FORBIDDEN
                )

        except Exception as e:
            print(e)
            return Response(
                {
                    'success': False,
                    'message': str(e),
                    'details': 'Verifiy OTP Failed'
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


# logout api view
class LogoutView(APIView):
    permission_classes = (permissions.IsAuthenticated)

    def post(self, request, format=None):
        try:
            request.user.auth_token.delete()
            return Response(
                {
                    'success': True,
                    'message': 'Logout successfully',
                    'status': status.HTTP_200_OK,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {
                    'success': False,
                    'message': str(e),
                    'status': status.HTTP_400_BAD_REQUEST,
                },
                status= status.HTTP_400_BAD_REQUEST,
            )