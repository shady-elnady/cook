# import base64
# from datetime import datetime
# from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.authentication import TokenAuthentication
# from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response

# from django.core.exceptions import ObjectDoesNotExist
# import pyotp

from .Serializer import UserLoginSerializer
from User.models import  User

# # Create your views here.


# # Class based view to Get User Details using Token Authentication
# class UserDetailAPI(APIView):
#   authentication_classes = (TokenAuthentication,)
#   permission_classes = (AllowAny,)
#   def get(self,request,*args,**kwargs):
#     user = User.objects.get(id=request.user.id)
#     serializer = UserSerializer(user)
#     return Response(serializer.data)




# class GenerateOTP(generics.GenericAPIView):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()

#     def post(self, request):
#         data = request.data
#         user_id = data.get('user_id', None)
#         email = data.get('email', None)

#         user = User.objects.filter(id=user_id).first()
#         if user == None:
#             return Response({"status": "fail", "message": f"No user with Id: {user_id} found"}, status=status.HTTP_404_NOT_FOUND)

#         otp_base32 = pyotp.random_base32()
#         otp_auth_url = pyotp.totp.TOTP(otp_base32).provisioning_uri(
#             username=email.lower(), issuer_name="codevoweb.com")

#         user.otp_auth_url = otp_auth_url
#         user.otp_base32 = otp_base32
#         user.save()

#         return Response({'base32': otp_base32, "otpauth_url": otp_auth_url})


# class VerifyOTP(generics.GenericAPIView):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()

#     def post(self, request):
#         message = "Token is invalid or user doesn't exist"
#         data = request.data
#         user_id = data.get('user_id', None)
#         otp_token = data.get('token', None)
#         user = User.objects.filter(id=user_id).first()
#         if user == None:
#             return Response({"status": "fail", "message": f"No user with Id: {user_id} found"}, status=status.HTTP_404_NOT_FOUND)

#         totp = pyotp.TOTP(user.otp_base32)
#         if not totp.verify(otp_token):
#             return Response({"status": "fail", "message": message}, status=status.HTTP_400_BAD_REQUEST)
#         user.otp_enabled = True
#         user.otp_verified = True
#         user.save()
#         serializer = self.serializer_class(user)

#         return Response({'otp_verified': True, "user": serializer.data})


# class ValidateOTP(generics.GenericAPIView):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()

#     def post(self, request):
#         message = "Token is invalid or user doesn't exist"
#         data = request.data
#         user_id = data.get('user_id', None)
#         otp_token = data.get('token', None)
#         user = User.objects.filter(id=user_id).first()
#         if user == None:
#             return Response({"status": "fail", "message": f"No user with Id: {user_id} found"}, status=status.HTTP_404_NOT_FOUND)

#         if not user.otp_verified:
#             return Response({"status": "fail", "message": "OTP must be verified first"}, status=status.HTTP_404_NOT_FOUND)

#         totp = pyotp.TOTP(user.otp_base32)
#         if not totp.verify(otp_token, valid_window=1):
#             return Response({"status": "fail", "message": message}, status=status.HTTP_400_BAD_REQUEST)

#         return Response({'otp_valid': True})


# class DisableOTP(generics.GenericAPIView):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()

#     def post(self, request):
#         data = request.data
#         user_id = data.get('user_id', None)

#         user = User.objects.filter(id=user_id).first()
#         if user == None:
#             return Response({"status": "fail", "message": f"No user with Id: {user_id} found"}, status=status.HTTP_404_NOT_FOUND)

#         user.otp_enabled = False
#         user.otp_verified = False
#         user.otp_base32 = None
#         user.otp_auth_url = None
#         user.save()
#         serializer = self.serializer_class(user)

#         return Response({'otp_disabled': True, 'user': serializer.data})




# # This class returns the string needed to generate the key
# class generateKey:
#     @staticmethod
#     def returnValue(phone):
#         return str(phone) + str(datetime.date(datetime.now())) + "Some Random Secret Key"



# class MobileVerifyOTP(generics.GenericAPIView):
#     queryset = Mobile.objects.all()
#     serializer_class = MobileSerializer
#     permission_classes = [
#         AllowAny,
#         # IsAuthenticated,
#     ]

#     # Get to Create a call for OTP
#     def get_queryset(self):
#         phone = self.kwargs['mobile']
#         try:
#             Mobile = Mobile.objects.get(mobile=phone)  # if Mobile already exists the take this else create New One
#         except ObjectDoesNotExist:
#             Mobile.objects.create(
#                 owner= self.request.user,
#                 mobile=phone,
#             )
#             Mobile = Mobile.objects.get(mobile=phone)  # user Newly created Model
#         Mobile.counter += 1  # Update Counter At every Call
#         Mobile.save()  # Save the data
#         keygen = generateKey()
#         key = base64.b32encode(keygen.returnValue(phone).encode())  # Key is generated
#         OTP = pyotp.HOTP(key)  # HOTP Model for OTP is created
#         print(OTP.at(Mobile.counter))
#         # Using Multi-Threading send the OTP Using Messaging Services like Twilio or Fast2sms
#         return Response({"OTP": OTP.at(Mobile.counter)}, status=200)  # Just for demonstration

#     # This Method verifies the OTP
#     def post(self, request):
#         data = request.data
#         user_id = data.get('user_id', None)
#         # user_id = request.POST['user_id']
#         phone = data.get('mobile', None)

#         user = User.objects.filter(id__iexact=user_id).first()
#         if user == None:
#             return Response(
#                 {"status": "fail", "message": f"No user with Id: {user_id} found"}, 
#                 status=status.HTTP_404_NOT_FOUND,
#             )
#         try:
#             Mobile = Mobile.objects.get(
#                 # owner= user,
#                 mobile=phone,
#             )
#         except ObjectDoesNotExist:
#             return Response("User does not exist", status=404)  # False Call

#         keygen = generateKey()
#         key = base64.b32encode(keygen.returnValue(phone).encode())  # Generating Key
#         OTP = pyotp.HOTP(key)  # HOTP Model
#         if OTP.verify(request.data["otp"], Mobile.counter):  # Verifying the OTP
#             Mobile.isVerified = True
#             Mobile.save()
#             # user.otp_enabled = False
#             # user.otp_verified = False
#             # user.otp_base32 = None
#             # user.otp_auth_url = None
#             # mobile = user.Mobile
#             # mobile.is_verified = False
#             # mobile.save()
#             # user.save()
#             serializer = self.serializer_class(user)
#             return Response({'otp_verified': True, 'user': serializer.data, 'message': 'You are authorised' }, status=200)
#         return Response("OTP is wrong", status=400)

# # Time after which OTP will expire
# EXPIRY_TIME = 50 # seconds

# class MobileVerifyOTPTimeBased(generics.GenericAPIView):
#     queryset = Mobile.objects.all()
#     serializer_class = MobileSerializer
#     permission_classes = [
#         AllowAny,
#         # IsAuthenticated,
#     ]

#     # Get to Create a call for OTP
#     def get_queryset(self):
#         phone = self.kwargs['mobile']
#         try:
#             Mobile = Mobile.objects.get(mobile=phone)  # if Mobile already exists the take this else create New One
#         except ObjectDoesNotExist:
#             Mobile.objects.create(
#                 owner= self.request.user,
#                 mobile=phone,
#             )
#             Mobile = Mobile.objects.get(mobile=phone)  # user Newly created Model
#         Mobile.save()  # Save the data
#         keygen = generateKey()
#         key = base64.b32encode(keygen.returnValue(phone).encode())  # Key is generated
#         OTP = pyotp.TOTP(key,interval = EXPIRY_TIME)  # TOTP Model for OTP is created
#         print(OTP.now())
#         # Using Multi-Threading send the OTP Using Messaging Services like Twilio or Fast2sms
#         return Response({"OTP": OTP.now()}, status=200)  # Just for demonstration

#     # This Method verifies the OTP
#     def post(self, request):
#         data = request.data
#         user_id = data.get('user_id', None)
#         phone = data.get('mobile', None)

#         user = User.objects.filter(id=user_id).first()
#         if user == None:
#             return Response(
#                 {"status": "fail", "message": f"No user with Id: {user_id} found"}, 
#                 status=status.HTTP_404_NOT_FOUND,
#             )
#         try:
#             Mobile = Mobile.objects.get(
#                 # owner= user,
#                 mobile=phone,
#             )
#         except ObjectDoesNotExist:
#             return Response("User does not exist", status=404)  # False Call

#         keygen = generateKey()
#         key = base64.b32encode(keygen.returnValue(phone).encode())  # Generating Key
#         OTP = pyotp.TOTP(key,interval = EXPIRY_TIME)  # TOTP Model 
#         if OTP.verify(request.data["otp"]):  # Verifying the OTP
#             Mobile.isVerified = True
#             Mobile.save()
#             # user.otp_enabled = False
#             # user.otp_verified = False
#             # user.otp_base32 = None
#             # user.otp_auth_url = None
#             # mobile = user.Mobile
#             # mobile.is_verified = False
#             # mobile.save()
#             # user.save()
#             serializer = self.serializer_class(user)
#             return Response({'otp_verified': True, 'user': serializer.data, 'message': 'You are authorised' }, status=200)
#         return Response("OTP is wrong/expired", status=400)




#   @api_view(['POST'])
# def register(request):
#     userser = SignUpUserSerialzer(data=request.data)
#     if userser.is_valid():
#         user = userser.save(is_active = False)
#         activateEmail(request, user, userser.validated_data['email'])
#         return Response(userser.data)

#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)


# @api_view(['POST'])
# def logIn(request):
#     username=request.data['username_or_email']
#     password=request.data['password']
    
#     print(username)
#     print(password)
#     try :
#         user = authenticate(username=username, password=password)
#         print('login')
#         print(user)
#         if user is not None:
#             # login(request, user)
#             return Response(
#                 {
#                     "success": True,
#                     "meassage": "Log In Success",
#                     "data": user,
#                 },
#                 status=status.HTTP_202_ACCEPTED,
#             )
#         else:
#             return Response(
#                 {
#                     "success": False,
#                     "meassage": "User Not Found .you must Registeres",
#                 },
#                 status=status.HTTP_401_UNAUTHORIZED,
#             )
#     except :
#         return Response(
#             {
#                 "success": False,
#                 "meassage": "User Not Found .you must Registeres",
#             },
#             status=status.HTTP_401_UNAUTHORIZED,
#         )




class UserLoginView(RetrieveAPIView):

    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'User logged in  successfully',
            }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)

# def activateEmail(request, user, to_email):
#     mail_subject = 'Activate your user account.'
#     message = render_to_string('template_activate_account.html', {
#         'user': user.username,
#         'domain': get_current_site(request).domain,
#         'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#         'token': account_activation_token.make_token(user),
#         'protocol': 'https' if request.is_secure() else 'http'
#     })
#     email = EmailMessage(mail_subject, message, to=[to_email])
#     if email.send():
#         messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
#             received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
#     else:
#         messages.error(request,
#             f'Problem sending confirmation email to {to_email}, check if you typed it correctly.')

# @api_view(['GET'])
# def activate(request, uidb64, token):
#     User = get_user_model()
#     try:
#         uid = force_str(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except(TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None

#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()
#         return Response('account activated')
#     else:
#         return Response('activation failed')