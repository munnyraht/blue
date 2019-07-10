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

class bvn_details(models.Model):
    email=models.EmailField(null=True)
    bvn=models.IntegerField()
    first_name=models.CharField(max_length=38, null=True)
    last_name= models.CharField(max_length=38, null=True)
    middle_name=models.CharField(max_length=38, null=True)
    date_of_birth=models.DateField()
    phone_number=models.IntegerField()
    registration_date=models.DateField()
    enrollment_bank=models.IntegerField()
    enrollment_branch=models.CharField(max_length=38, null=True)
    

