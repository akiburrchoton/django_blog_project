from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user    = models.OneToOneField(User, on_delete=models.CASCADE) # Cascade - User is deleted - Delete the profile but if profile is deleted - don't delete the user
    image   = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile' 