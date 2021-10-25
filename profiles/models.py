from django.db import models 
from django.conf import settings
from django.utils.translation import gettext_lazy as _ 

AUTH_USER_MODEL  = getattr(settings, "AUTH_USER_MODEL", "auth.User")

def get_image_path(instance, filename):
    pass


class Profile(models.Model): 
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="auth_user_profiles")
    
    def __str__(self):
        return self.user.username 

