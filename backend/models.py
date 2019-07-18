from django.db import models
from users.models import BluecreditUser

# Create your models here.
# class user(models.Model):
#     FirstName=models.CharField(max_length=38, null=True)
#     Surname = models.CharField(max_length=38, null=True)
#     Role=models.CharField(max_length=38,null=True)
#     EmailAddress=models.EmailField(null=True)
#     MobileNumber=models.DecimalField(decimal_places=0, max_digits=11,null=True)
#     Password=models.CharField(max_length=38,null=True)
#     active = models.CharField(max_length=100, default='pending')
#     ConfirmPassword=models.CharField(max_length=38,null=True)
#     Created = models.DateTimeField(auto_now = True,)



class bvn_details(models.Model):

    email=models.ForeignKey(BluecreditUser, on_delete=models.PROTECT)
    bvn=models.IntegerField(null=True)
    first_name=models.CharField(max_length=38, null=True)
    last_name= models.CharField(max_length=38, null=True)
    middle_name=models.CharField(max_length=38, null=True)
    date_of_birth=models.DateField(null=True)
    phone_number=models.IntegerField(null=True)
    registration_date=models.DateField(null=True)
    enrollment_bank=models.IntegerField(null=True)
    enrollment_branch=models.CharField(max_length=38, null=True)

class personalinfo(models.Model):

    email=models.ForeignKey(BluecreditUser, on_delete=models.PROTECT)
    MiddleName= models.CharField(max_length=32)
    MobileNumber2=models.IntegerField(null=True)
    DateOfBirth=models.DateField(null=True)
    MaritalStatus=models.CharField(max_length=50)
    PlaceOfBirth=models.CharField(max_length=100)

    # NumberOfDependent=models.IntegerField()
    # DateAtAddress=models.DateField()
    # HomeAddress= models.TextField()
    # # objects = personalInfo()
    # # CreatedDate = models.DateTimeField(auto_now = True,)

    NumberOfDependent=models.IntegerField(null=True)
    DateAtAddress=models.DateField(null=True)
    HomeAddress= models.TextField(null=True)


    objects = models.Manager()


    

