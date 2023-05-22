from typing import TYPE_CHECKING, Optional

from django.contrib.auth.models import BaseUserManager
from django.db.models.manager import Manager



if TYPE_CHECKING:
    from .models import User


class UsersManager(BaseUserManager):
    def create_user(
        self, email: str, username: str,password: Optional[str] = None, **extra_fields
    ) -> "User":
        # if not email:
        #     raise ValueError("The Email must be set")
        values = [email, username]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
        
        for field_name, value in field_value_map.items():
            if not value:
                raise ValueError('The {} value must be set'.format(field_name))
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.is_active = True
        user.set_password(password)
        user.save()
        return user
    
    def create_staffuser(
        self, email: str, username: str, password: Optional[str] = None, **extra_fields
    )-> "User":
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        if extra_fields.get("is_staff") is False:
            raise ValueError("StaffUser must have is_staff=True.")      
        return self.create_user(email, username, password, **extra_fields)

    def create_superuser(
        self, email: str, username: str, password: Optional[str] = None, **extra_fields
    ) -> "User":
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is False:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, username, password, **extra_fields)