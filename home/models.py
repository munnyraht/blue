from django.db import models
from django.core.files.storage import FileSystemStorage
from backend.models import personalinfo
# from backend.models import user
from users.models import BluecreditUser
from django import forms
from backend.models import personalinformation
from django.core.files.images import ImageFile
from wagtail.core.models import Page


class HomePage(Page):

    pass

class HomeData(models.Model):
    yearlyloans = models.CharField(max_length=100, default='240,000')
    minimuminterest = models.CharField(max_length=100, default='15%')
    maxmonths = models.CharField(max_length=100, default='24')
    maxloan = models.CharField(max_length=100,default='1,000,000')
    customerservice = models.CharField(max_length=100, default='24/7')
    bluehostemail = models.CharField(max_length=100, default='info@bluecredit.com')
    phone = models.IntegerField(default=+234808080808)


    # return render(request, 'home.html', context) 

class Create(models.Model):
    bvn = models.CharField(max_length=100, default='')


class Createnextofkin(models.Model):
    user_id=models.ForeignKey(BluecreditUser, on_delete=models.PROTECT, default='1')
    nextofkinname = models.CharField(max_length=100, default='240,000')
    nextofkinrelationship = models.CharField(max_length=100, default='15%')
    nextofkinaddress = models.CharField(max_length=100, default='24')
    nextofkinphone = models.CharField(max_length=100,default='1,000,000')
    landmark = models.CharField(max_length=100, default='Eko Hotels')
    nextofkinemail = models.CharField(max_length=100, default='admin@mail.com')
    income = models.CharField(max_length=100, default='1 million')



class EmploymentDetails(models.Model):
    user_id=models.ForeignKey(BluecreditUser, on_delete=models.PROTECT, default='1')
    Bankname = models.CharField(max_length=100, default='Bankname')
    Existing_bank_account_number = models.CharField(max_length=100, default='0000000')
    Highest_level_of_education = models.CharField(max_length=100, default='Degree')
    Employment_status = models.CharField(max_length=100,default='employed')
    Current_employer = models.CharField(max_length=100, default='Mr Wale')
    Employers_address_and_department = models.CharField(max_length=100, default='CEO')
    Landmark_closest_to_address = models.CharField(max_length=100, default='Eko')
    Income = models.CharField(max_length=100, default='1 million')
    Net_monthly_income_with_tax = models.CharField(max_length=100, default='1 million')

class AdditionalInformation(models.Model):
    user_id=models.ForeignKey(BluecreditUser, on_delete=models.PROTECT, default='1')
    Official_email_address = models.CharField(max_length=100, default='email@mail.com')
    Official_pay_day = models.CharField(max_length=100, default='0000000')
    Loan_amount = models.CharField(max_length=100, default='Degree')
    Tenor_agreed = models.CharField(max_length=100,default='employed')
    Number_of_cheques_submitted = models.CharField(max_length=100, default='Mr Wale')
    Account_name = models.CharField(max_length=100, default='CEO')
    NUBAN_account_number = models.CharField(max_length=100, default='Eko')
    Bank_name = models.CharField(max_length=100, default='Zenith')
    Net_monthly_income = models.CharField(max_length=100, default='1 million')
    Amount_requested = models.CharField(max_length=100, default='1 million')


class Personaldetails(models.Model):
    user_id=models.ForeignKey(BluecreditUser, on_delete=models.PROTECT, default='1')
    firstname = models.CharField(max_length=100, default='240,000')
    surname = models.CharField(max_length=100, default='15%')
    middlename = models.CharField(max_length=100, default='24')
    mobilephone = models.CharField(max_length=100,default='1,000,000')
    title = models.CharField(max_length=100, default='Eko Hotels')
    dateofbirth = models.CharField(max_length=100, default='admin@mail.com')
    maritalstatus = models.CharField(max_length=100, default='1 million')
    email = models.CharField(max_length=100, default='24')
    timeataddress = models.CharField(max_length=100,default='1,000,000')
    other = models.CharField(max_length=100, default='Eko Hotels')
    numberofdependents = models.CharField(max_length=100, default='admin@mail.com')
    placeofbirth = models.CharField(max_length=100, default='1 million')
    homeaddress = models.CharField(max_length=100, default='1 million')
    timestamp = models.DateTimeField(auto_now = True,)


class Contact(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name


class Acknowledgement(models.Model):
    user_id=models.ForeignKey(BluecreditUser, on_delete=models.PROTECT, default='1')
    terms_and_conditions = models.CharField(max_length=255, blank=True)
    how_you_heard_about_us = models.CharField(max_length=255, blank=True)
    signature = models.ImageField(upload_to='signatures/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
