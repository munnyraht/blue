from django.db import models
from django import forms

# Create your models here.
class user(models.Model):
    FirstName=models.CharField(max_length=38, null=True)
    Surname = models.CharField(max_length=38, null=True)
    Role=models.CharField(max_length=38,null=True)
    EmailAddress=models.EmailField(null=True)
    MobileNumber=models.DecimalField(decimal_places=0, max_digits=11,null=True)
    Password=models.CharField(max_length=38,null=True)
    ConfirmPassword=models.CharField(max_length=38,null=True)
