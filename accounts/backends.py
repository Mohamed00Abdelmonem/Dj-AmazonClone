from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class EmailOrUsernameModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()

        try:
            # Check if the input is an email
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            try:
                # Check if the input is a username
                user = UserModel.objects.get(username=username)
            except UserModel.DoesNotExist:
                return None

        # Check the user's password
        if user.check_password(password):
            return user

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
