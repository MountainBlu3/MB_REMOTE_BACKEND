from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import authenticate

class StaffBackend(BaseBackend):
    def authenticate(self, request, staff_id=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(staff_id=staff_id)
        except UserModel.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None

