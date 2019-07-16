from django.db import models

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
    nextofkinname = models.CharField(max_length=100, default='240,000')
    nextofkinrelationship = models.CharField(max_length=100, default='15%')
    nextofkinaddress = models.CharField(max_length=100, default='24')
    nextofkinphone = models.CharField(max_length=100,default='1,000,000')
    landmark = models.CharField(max_length=100, default='Eko Hotels')
    nextofkinemail = models.CharField(max_length=100, default='admin@mail.com')
    income = models.CharField(max_length=100, default='1 million')


