from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_Link=models.URLField(blank=True)
    picture=models.ImageField(upload_to='profile_pic')

    def __str__(self):
        return self.user.username
