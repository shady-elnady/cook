from django.contrib.auth import authenticate

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from .models import User, Profile, UserRestaurant
from .Serializer import (
    UserSerializer,
    ProfileSerializer,
    UserRestaurantSerializer,
)



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



class ProfileViewSet(ModelViewSet):
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