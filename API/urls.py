from django.urls import path, re_path, include
from rest_framework.authtoken import views

from .views import (
  UserLoginView, MobileSendOTP, VerifymobileOTPView, LogoutView,
  register_by_access_token,
)


app_name = "API"


urlpatterns = [
  # path('auth/login/', LoginView.as_view(), name='Auth_LogIn'),
  path('login/',  UserLoginView.as_view(), name='Auth_LogIn'),
  path('get-otp-mobile/',MobileSendOTP.as_view(),name='get-OTP-Mobile'),
  path('verify-otp-mobile/',VerifymobileOTPView.as_view(),name='OTP-Verify'),
  re_path('register-by-access-token/' + r'social/(?P<backend>[^/]+)/$', register_by_access_token, name= "RegisterByToken"),
  path('social-auth/', include('social_django.urls', namespace="social")),
  path('log_out/', LogoutView.as_view(), name= "LogOut"),
]


"""
  https://codevoweb.com/django-implement-2fa-two-factor-authentication/

"""