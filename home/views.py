from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from home.models import HomeData
from home.models import Create
from home.models import Createnextofkin
from django.http import HttpResponse
# from django.core.mail import send_mail
from django.conf import settings
from backend.models import user, bvn_details,personalInfo
from backend import views 
from backend.forms import Bvn_number,personalInfo
from home.functions import get_bvn_details
from django.contrib import messages


def home(request):
	homedata = HomeData.objects.all()
	template = 'home/welcome_page.html'
	return render(request, template, {'homedata': homedata})


def loantype(request):
	context = {}
	template = 'loantype/loantype.html'
	return render(request, template, context)


def loansummary(request):
	context = {}
	template = 'loantype/loansummary.html'
	return render(request, template, context)

def paymentinfo(request,email='muniratsulaimon@gmail.com'):
	user_details= user.objects.get(EmailAddress=email)
	if request.method=='POST':
		form=personalInfo(request.POST)
		if form.is_valid():
			obj=form.cleaned_data
			MiddleName= obj['MiddleName']
			MobileNumber2=obj['MobileNumber2']
			DateOfBirth=obj['DateOfBirth']
			MaritalStatus=obj['MaritalStatus']
			PlaceOfBirth=obj['PlaceOfBirth']
			NumberOfDependent=obj['NumberOfDependent']
			DateAtAddress=obj['DateAtAddress']
			HomeAddress= obj['HomeAddress']
			personalInfo.objects.create(EmailAddress=email,MiddleName=MiddleName,MobileNumber2=MobileNumber2,DateOfBirth=DateOfBirth,MaritalStatus=MaritalStatus,PlaceOfBirth=PlaceOfBirth,NumberOfDependent=NumberOfDependent,DateAtAddress=DateAtAddress,HomeAddress=HomeAddress)
			template = 'nextofkin'
			#return render(request, template, context)
			return redirect(template)
	else:
		form=personalInfo()
		context = {'user_details': user_details, 'form': form}
		template = 'paymentinfo/paymentinfo.html'
		return render(request, template, context)

def otherdetails(request):
	context = {}
	template = 'paymentinfo/otherdetails.html'
	return render(request, template, context)

def summary(request):
	context = {}
	template = 'paymentinfo/summary.html'
	return render(request, template, context)

def employmentinfo(request):
	context = {}
	template = 'paymentinfo/employmentinfo.html'
	return render(request, template, context)

def nextofkin(request):
	nextofkindata = Createnextofkin.objects.all()
	context = {}
	template = 'paymentinfo/nextofkin.html'
	return render(request, template, {'nextofkindata': nextofkindata})


def bvnerror(request):
	context = {}
	template = 'bvnerror/bvnerror.html'
	return render(request, template, context)

# def verifybvn(request):
# 	form = Bvn_number()
# 	context = {'form':form}
# 	template = 'bvnerror/verifybvn.html'
# 	return render(request, template, context)

def verifybvn(request):
	if (request.method=='POST'):
		form=Bvn_number(request.POST)
		if form.is_valid():
			userObj = form.cleaned_data
			bvn_number = userObj['Bvn_Number']
			email=userObj['EmailAddress']
			response=get_bvn_details(bvn_number)
			if response['status']!= 'success':
				messages.error(request, "something went wrong, try again")
				return render(request,'bvnerror/verifybvn.html',{})
			else:
				bvn=response['data']['bvn']
				first_name=response['data']['first_name']
				last_name= response['data']['last_name']
				middle_name=response['data']['middle_name']
				date_of_birth=response['data']['date_of_birth']
				phone_number=response['data']['phone_number']
				registration_date=response['data']['registration_date']
				enrollment_bank=response['data']['enrollment_bank']
				enrollment_branch=response['data']['enrollment_branch']
				bvn_details.objects.create(email=email,bvn=bvn,first_name=first_name,last_name=last_name,middle_name=middle_name,date_of_birth = date_of_birth, phone_number=phone_number, registration_date=registration_date,enrollment_bank=enrollment_bank, enrollment_branch=enrollment_branch)
				return redirect('bvnerror/bvnaccepted.html', email=email)
	else:
		form = Bvn_number()
		context = {'form':form}
		template = 'bvnerror/verifybvn.html'
		return render(request, template, context)


def bvnaccepted(request,email):
	context = {'email':email}
	template = 'bvnerror/bvnaccepted.html'
	return render(request, template, context)

def acknowledgement(request):
	context = {}
	template = 'acknowledgement/acknowledgement.html'
	return render(request, template, context)

# def create(request):
# 	if request.method == 'POST':
# 		bvn = request.POST['bvn']


# 		Create.objects.create(
# 			bvn = bvn
			
# 		)

# 		return HttpResponse('')


def create(request):
    create = Create(bvn=request.POST['bvn'])
    create.save()
    return redirect('bvnaccepted')


def createnextofkin(request):
    createnextofkin = Createnextofkin(
    	nextofkinname=request.POST['nextofkinname'],
    	nextofkinrelationship=request.POST['nextofkinrelationship'],
    	nextofkinaddress=request.POST['nextofkinaddress'],
    	nextofkinphone=request.POST['nextofkinphone'],
    	landmark=request.POST['landmark'],
    	nextofkinemail=request.POST['nextofkinemail'],
    	income=request.POST['income'],

    	)
    createnextofkin.save()
    return redirect('acknowledgement/acknowledgement.html')


