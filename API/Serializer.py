import re
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework.serializers import (
    ModelSerializer,
    Serializer,
    EmailField,
    CharField,
    ValidationError,
 )
from rest_framework.validators import UniqueValidator
from django.utils.translation import gettext_lazy as _
from rest_framework.response import Response
from rest_framework import status, generics

import imp
from rest_framework import serializers
from django.contrib.auth import get_user_model
from User.check_email import check_is_email
# from accounts.models import Role
from User.models import User


# User = get_user_model()

class RegisterSerializer(ModelSerializer):
    username = CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all(), message= _("User Name Used. chosse Another"))],
    )
    email = EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all(), message= _("E-Mail is Exced."))],
    )
    password = CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
    )
    
    def create(self, validated_data):
        user = User.objects.create(
        **validated_data
        )
        user.set_password(validated_data['password'])
        user.save()
        return user    
    
    class Meta:
        model = User
        fields = [
            'username', "email", 'password',           
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "username": {"required": True},
            "email": {"required": True},
            "password": {"required": True},
            "mobile": {"required": False},
        }



class UserLoginSerializer(serializers.Serializer):

    username_or_email = serializers.CharField(max_length=255, required=True, source='username')
    password = serializers.CharField(max_length=128, write_only=True, required=True,)

    def validate(self, data):
        # username = data['username']
        return data
    
    class Meta:
        model = User
        fields = ['username', 'email']

        