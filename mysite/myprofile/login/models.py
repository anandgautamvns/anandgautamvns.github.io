from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,blank=True)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic',blank=True)
    department = models.CharField(max_length=50)
    employee_name = models.CharField(max_length=50)
    age = models.IntegerField(blank=True)
    address = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.user.username
