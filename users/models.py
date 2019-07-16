
from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms

class BluecreditUser(AbstractUser, models.Model):
    # pass
    FirstName=models.CharField(max_length=38, null=True)
    Surname = models.CharField(max_length=38, null=True)
    Role=models.CharField(max_length=38,null=True)
    EmailAddress=models.EmailField(null=True)
    MobileNumber=models.DecimalField(decimal_places=0, max_digits=11,null=True)
    # Password=models.CharField(max_length=38,null=True)
    active = models.CharField(max_length=100, default='pending')
    # ConfirmPassword=models.CharField(max_length=38,null=True)
    Created = models.DateTimeField(auto_now = True,)