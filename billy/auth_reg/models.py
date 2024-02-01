from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    # username = models.CharField(max_length=255)
    # password = models.CharField(max_length=255)
    # confirm_password = models.CharField(max_length=255)
    
    def __str__(self):
        return self.user.username