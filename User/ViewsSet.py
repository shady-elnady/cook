import base64
from datetime import datetime
from django.contrib.auth import authenticate

from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist

from .models import User, Profile, UserRestaurant
from .Serializer import (
    UserSerializer,
    ProfileSerializer,
    UserRestaurantSerializer,
)
# import pyotp



class UserViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

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

    def get_queryset(self):
        return Profile.objects.all().filter(user=self.request.user)


class UserRestaurantViewSet(ModelViewSet):
    queryset = UserRestaurant.objects.all()
    serializer_class = UserRestaurantSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserRestaurant.objects.all().filter(user=self.request.user)


#######################################################################################




# class GenerateOTPViewSet(ModelViewSet):
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




# class VerifyOTPViewSet(ModelViewSet):
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


# class ValidateOTPViewSet(ModelViewSet):
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


# class DisableOTPViewSet(ModelViewSet):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()

#     def post(self, request):
#         data = request.data
#         user_id = data.get('user_id', None)

#         user = User.objects.filter(id=user_id).first()
#         if user == None:
#             return Response(
#                 {"status": "fail", "message": f"No user with Id: {user_id} found"}, 
#                 status=status.HTTP_404_NOT_FOUND,
#             )
#         user.otp_enabled = False
#         user.otp_verified = False
#         user.otp_base32 = None
#         user.otp_auth_url = None
#         mobile = user.Mobile
#         mobile.is_verified = False
#         mobile.save()
#         user.save()
#         serializer = self.serializer_class(user)
#         return Response({'otp_disabled': True, 'user': serializer.data})


# # This class returns the string needed to generate the key
# class generateKey:
#     @staticmethod
#     def returnValue(phone):
#         return str(phone) + str(datetime.date(datetime.now())) + "Some Random Secret Key"


# class MobileVerifyOTPViewSet(ModelViewSet):
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

# class MobileVerifyOTPTimeBasedViewSet(ModelViewSet):
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



# from rest_framework.exceptions import PermissionDenied


# class PollViewSet(viewsets.ModelViewSet):
#     # ...

#     def destroy(self, request, *args, **kwargs):
#         poll = Poll.objects.get(pk=self.kwargs["pk"])
#         if not request.user == poll.created_by:
#             raise PermissionDenied("You can not delete this poll.")
#         return super().destroy(request, *args, **kwargs)


# class ChoiceList(generics.ListCreateAPIView):
#     # ...

#     def post(self, request, *args, **kwargs):
#         poll = Poll.objects.get(pk=self.kwargs["pk"])
#         if not request.user == poll.created_by:
#             raise PermissionDenied("You can not create choice for this poll.")
#         return super().post(request, *args, **kwargs)