from django.urls import path, include
from rest_framework.authtoken import views

from .views import (
   UserLoginView, MobileSendOTP, VerifymobileOTPView, LogoutView, change_password, passwordRecovery, verify_email,
)


app_name = "API"


urlpatterns = [
  path('login/',  UserLoginView.as_view(), name='Auth_LogIn'),
  path('get-otp-mobile/',MobileSendOTP.as_view(),name='get_OTP_Mobile'),
  path('verify-otp-mobile/',VerifymobileOTPView.as_view(),name='OTP_Verify'),
  path('change-password/', change_password, name='Change_Password'),
  path('password-recovery/', passwordRecovery.as_view(), name='Password_Recovery'),
  path('verify-email/<int:pk>/', verify_email, name='Verify_E-mail'),
  path('logout/', LogoutView.as_view(), name= "LogOut"),
]


"""
  https://codevoweb.com/django-implement-2fa-two-factor-authentication/

  https://studygyaan.com/tag/django-rest-framework

"""