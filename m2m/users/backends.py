import logging
from django.conf import settings
#from django.contrib.auth.models import User
from users.models import User

class Login:

    """
    Authenticate against a user on an LDAP server.
    """

    def authenticate(self, username, password):
        user = User.objects.get(username=username, password=password)
        return user    
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
        
