from django.db import models
from django.contrib.auth.models import User


#extended user model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    timezone = models.CharField(max_length = 24)