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
    email=models.ForeignKey(user, on_delete=models.PROTECT)
    bvn=models.IntegerField()
    first_name=models.CharField(max_length=38, null=True)
    last_name= models.CharField(max_length=38, null=True)
    middle_name=models.CharField(max_length=38, null=True)
    date_of_birth=models.DateField()
    phone_number=models.IntegerField()
    registration_date=models.DateField()
    enrollment_bank=models.IntegerField()
    enrollment_branch=models.CharField(max_length=38, null=True)

class personalInfo(models.Model):
    email=models.ForeignKey(user, on_delete=models.PROTECT)
    MiddleName= models.CharField(max_length=32)
    MobileNumber2=models.IntegerField()
    DateOfBirth=models.DateField()
    MaritalStatus=models.CharField(max_length=50)
    PlaceOfBirth=models.CharField(max_length=100)
    NumberOfDependent=models.IntegerField()
    DateAtAddress=models.DateField()
    HomeAddress= models.TextField()

    

