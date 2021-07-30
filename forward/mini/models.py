from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    occupation = models.TextField(blank=True)
    company = models.TextField(blank=True)
    hobby = models.TextField(blank=True)

    def __str__(self):
        return self.user.username