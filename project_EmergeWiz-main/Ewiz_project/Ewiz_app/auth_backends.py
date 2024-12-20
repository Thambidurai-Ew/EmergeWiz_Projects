# backends.py
from django.contrib.auth.backends import BaseBackend
from django.db.models import Q
from .models import NewUser
from .utils import encrypt_password, decrypt_password
from django.contrib.auth import login

class MultiModelBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        print(f"Attempting to authenticate email: {email}")
        if email is None:
            print("No email provided for authentication")
        else:
            try:
                print("Looking up user by email:", email)
                user = NewUser.objects.get(Q(email=email))
                print("User found:", user)
                if decrypt_password(user.password) == password:
                    print("Authenticated as NewUser")
                    # Ensure 'request' is not None before using it
                    if not hasattr(user, 'backend'):
                        user.backend = 'Ewiz_app.auth_backends.MultiModelBackend'
                    return user
            except NewUser.DoesNotExist:
                print("NewUser does not exist")

        print("Authentication failed")
        return None
