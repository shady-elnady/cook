from django.conf import settings
from .models import User



class EmailOrUsernameModelBackend(object):
    def authenticate(self, username=None, password=None, email=None):
        if '@' in username:
            kwargs = {'email': username}
            kwargs = {'username': username}
        else:
            kwargs = {'username': username}
            kwargs = {'email': email}
        try:
            user = User.objects.get(**kwargs)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None



### and for case-insensitive :

# class EmailOrUsernameModelBackend(object):
#     def authenticate(self, username=None, password=None):
#         # user_model = get_user_model()
#         if '@' in username:
#             # kwargs = {'email': username}
#             field = 'email'
#         else:
#             # kwargs = {'username': username}
#             field = 'username'
#         try:
#             case_insensitive_username_field = '{}__iexact'.format(field)
#             user = User._default_manager.get(**{case_insensitive_username_field: username})

#             # user = User.objects.get(**kwargs)
#             if user.check_password(password):
#                 return user
#         except User.DoesNotExist:
#             return None

#     def get_user(self, user_id):
#         try:
#             return User.objects.get(pk=user_id)
#         except User.DoesNotExist:
#             return None