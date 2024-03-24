# In profiles/models.py

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    picture = models.ImageField(
        upload_to='profile_pictures/', blank=True, null=True)  # Add this line

    def __str__(self):
        return self.user.username
