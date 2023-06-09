import base64
from datetime import datetime
from email.message import EmailMessage
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework import status, generics
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser 
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from requests.exceptions import HTTPError
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model

from API.TwilioMessageHandler import TwilioMessageHandler
from API.Utils import otp_generator
from User.check_email import check_is_email
from .Serializer import LoginSerializer

# # Create your views here.

User = User = get_user_model()

class UserLoginView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        username_or_email = str(request.data["username_or_email"])
        password = str(request.data["password"])
        try:
            user = User.objects.filter(username=username_or_email).first()
            if user is None:
                user = User.objects.filter(email=username_or_email).first()

            if user is None or not user.check_password(password):
                return Response(
                    {
                        'success': False,
                        'message': 'User Not Found',
                        'status': status.HTTP_400_BAD_REQUEST,
                    },
                    status= status.HTTP_400_BAD_REQUEST,
                )
            else:
                # login(request, user=user)
                # token, _ = Token.objects.get_or_create(user=user)
                # token = Token.objects.get_or_create(user=user)[0].key
                return Response(
                    {
                        'success' : True,
                        'status code' : status.HTTP_200_OK,
                        'message': 'User logged successfully',
                        # 'token': token.key,
                        'data': {
                            "user_id": user.id,
                            "username": user.username,
                            "email": user.email,
                            "is_verified": user.is_verified,
                        },
                    },
                    status= status.HTTP_200_OK,
                )
        except Exception as e:
            return Response(
                {
                    'success': False,
                    'message': f'Error is {e}, with type {type(e)}',
                    'status': status.HTTP_400_BAD_REQUEST,
                },
                status= status.HTTP_400_BAD_REQUEST,
            )



"""
        curl -X POST \
        http://127.0.0.1/api/register-by-access-token/social/google-oauth2/ \
        -H 'Accept: application/json' \
        -H 'Content-Type: application/json' \
        -d '{"access_token": "<GoogleOAuth2-ACCESS-TOKEN-FROM-CLIENT>"}'

"""



@permission_classes([AllowAny])
class MobileSendOTP(APIView):

    def post(self, request, *agrs, **kwargs):
        try:
            mobile_number = str(request.data.get('mobile'))
            user_id = str(request.data.get('user_id'))
            methodOtp = str(request.data.get('methodOtp'))
            if mobile_number and user_id:
                mobile = str(mobile_number)
                user = User.objects.get(id__iexact=user_id)
                # otp_key = otp_generator()
                otp_key = "12345"
                if user is not None:
                    messagehandler = None               
                    if methodOtp=="methodOtpWhatsapp":
                        messagehandler=TwilioMessageHandler(mobile,otp_key).send_otp_via_whatsapp()
                    else:
                        messagehandler=TwilioMessageHandler(mobile,otp_key).send_otp_via_message()
                    if messagehandler is None:
                        return Response(
                            {
                                'success': False,
                                'message': 'Error Connection To Server',
                                'status': status.HTTP_404_NOT_FOUND,
                            },
                            status= status.HTTP_400_BAD_REQUEST,
                        )
                    else:
                        user.otp = otp_key
                        user.mobile = mobile
                        user.save()
                        return Response(
                            {
                                'success': True,
                                'message': 'Succes send OTP Go To Your Mobile',
                                'status': status.HTTP_202_ACCEPTED,
                                'data': {
                                    "user_id":user.id,
                                    "is_verified": user.is_verified,
                                },
                            },
                            status= status.HTTP_202_ACCEPTED,
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
@permission_classes([AllowAny])
class VerifymobileOTPView(APIView):
    def post(self, request, format=None):
        try:
            otp = str(request.data.get('otp'))
            user_id = str(request.data.get('user_id'))
            if otp and user_id:
                user = User.objects.get(id__iexact=user_id)
                if user is None:
                    return Response(
                        {
                        'success': False,
                        'message': 'User does not exist'
                        }, 
                        status=status.HTTP_403_FORBIDDEN
                    )
                else:
                    if user.otp == otp:
                        user.is_verified = True
                        user.is_active = True
                        user.save()
                        login(request, user=user)
                        token, _ = Token.objects.get_or_create(user=user)
                        return Response(
                            {
                                'status': True,
                                'message': 'Login Successfully',
                                'token': token.key,
                                'data': {
                                    'id': user.id,
                                    'username': user.username,
                                    'email': user.email,
                                    'mobile': user.mobile,
                                    'is_verified': user.is_verified,
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
                },
                status=status.HTTP_400_BAD_REQUEST,
            )




# logout api view
@permission_classes([IsAuthenticated])
class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated)

    def post(self, request, format=None):
        try:
            # request.user.auth_token.delete()
            logout(request)
            user = User.objects.get(id__iexact= request.user.id)
            user.is_verified = False
            user.otp= None
            user.save()
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

