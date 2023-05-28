from django.urls import path
from rest_framework.authtoken import views

from .views import (
  UserLoginView, MobileSendOTP, VerifymobileOTPView, LogoutView,
)


app_name = "API"


urlpatterns = [
  path('login/',  UserLoginView.as_view(), name='Auth_LogIn'),
  path('get-otp-mobile/',MobileSendOTP.as_view(),name='get-OTP-Mobile'),
  path('verify-otp-mobile/',VerifymobileOTPView.as_view(),name='OTP-Verify'),
  path('logout/', LogoutView.as_view(), name= "LogOut"),
]


"""
  https://codevoweb.com/django-implement-2fa-two-factor-authentication/

"""