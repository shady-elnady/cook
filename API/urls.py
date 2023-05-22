from django.urls import path, include
from rest_framework.authtoken import views
from knox.views import LogoutAllView

from .views import UserLoginView

from .ViewsSet import MobileSendOTP, VerifymobileOTPView, LogoutView

app_name = "API"


urlpatterns = [
  # path('register',RegisterUserAPIView.as_view(), name= "Registeration"),
  # path('login/', LoginView.as_view(), name= "LogIn"),
  # path("get-my_details",UserDetailAPI.as_view(), name= "GetUserDetails"),
  # #########
  # path('register', RegisterView.as_view(), name = "Registeration"),
  # path('auth/login', LoginView.as_view(), name = "Auth_LogIn"),
  # path('otp/generate', GenerateOTP.as_view(), name = "Generate_OTP"),
  # path('otp/verify', VerifyOTP.as_view(), name = "Verify_OTP"),
  # path('otp/validate', ValidateOTP.as_view(), name = "Validate_OTP"),
  # path('otp/disable', DisableOTP.as_view(), name = "Disable_OTP"),
  # path("otp/mobile_generate/<mobile>/", MobileVerifyOTP.as_view(), name="OTP Mobile Gen"),
  # path("otp/mobile_generate/time_based/<mobile>/", MobileVerifyOTPTimeBased.as_view(), name="OTP Mobile Gen Time Based"),

  #####
  # path('auth/login/', LoginView.as_view(), name='Auth_LogIn'),
  path('auth/login/',  UserLoginView.as_view(), name='Auth_LogIn'),
  path('get-otp-mobile/',MobileSendOTP.as_view(),name='get-OTP-Mobile'),
  path('verify-otp-mobile/',VerifymobileOTPView.as_view(),name='OTP-Verify'),
  path('logout/', LogoutView.as_view(), name='knox_logout'),
  path('logoutall/', LogoutAllView.as_view(), name='knox_logoutall'),
]


"""

https://codevoweb.com/django-implement-2fa-two-factor-authentication/


"""