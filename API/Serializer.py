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

from User.models import User



class RegisterSerializer(ModelSerializer):
    email = EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    password = CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
    )
    password2 = CharField(
        write_only=True,
        required=True,
    )
    class Meta:
        model = User
        fields = ('username', 'password', 'password2','email')
        extra_kwargs = {
        # 'first_name': {'required': True},
        # 'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise ValidationError(
                {
                    "password": "Password fields didn't match.",
                },
            )
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
        username=validated_data['username'],
        email=validated_data['email'],
        # first_name=validated_data['first_name'],
        # last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user





class LoginSerializer(Serializer):
    """
    This serializer defines two fields for authentication:
      * username
      * password.
    It will try to authenticate the user with when validated.
    """
    email = EmailField(
        label="email",
        write_only=True
    )
    password = CharField(
        label="Password",
        # This will be used when the DRF browsable API is enabled
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )

    def validate(self, attrs):
        # Take username and password from request
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            # Try to authenticate the user using Django auth framework.
            user = authenticate(
                request=self.context.get('request'),
                email=email,
                password=password,
            )
            if not user:
                # If we don't have a regular user, raise a ValidationError
                msg = 'Access denied: wrong username or password.'
                raise ValidationError(msg, code='authorization')
        else:
            msg = 'Both "Email" and "password" are required.'
            raise ValidationError(msg, code='authorization')
        # We have a valid user, put it in the serializer's validated_data.
        # It will be used in the view.
        attrs['user'] = user
        return attrs