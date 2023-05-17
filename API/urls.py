from django.urls import path
from rest_framework.authtoken import views

from .views import UserDetailAPI,RegisterUserAPIView, LoginView



app_name = "API"


urlpatterns = [
  path('register',RegisterUserAPIView.as_view(), name= "Registeration"),
  path('login/', LoginView.as_view(), name= "LogIn"),
  path("get-my_details",UserDetailAPI.as_view(), name= "GetUserDetails"),
]


## Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b