# from django.urls import path
# from django.contrib.auth.views import LogoutView, LoginView

# from .views import (
#   register_request,
#   # Twilio
#   register,
#   home,
#   otpVerify
# )


# app_name = "User"


# urlpatterns = [
#   path(
#     'login',
#     LoginView.as_view(
#       template_name = 'Log/log_in.html',
#       redirect_authenticated_user=True,
#     ),
#     name='LogIn',
#   ),
#   path("register", register_request, name="Register"),
#   path('logout/', LogoutView.as_view(), name='LogOut'),
#   # Twilio
#   path('twilio_register', register, name='TwilioRegister'),
#   # path('home', home, name='home'),
#   path('otp/<str:uid>/', otpVerify, name='otp')
# ]