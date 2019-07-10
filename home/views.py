from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from home.models import HomeData
from home.models import Create
from home.models import Createnextofkin
from django.http import HttpResponse
# from django.core.mail import send_mail
from django.conf import settings
from backend.models import user, bvn_details
from backend import views 
from backend.forms import Bvn_number
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

def paymentinfo(request):
	context = {}
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
		form=Bvn_number(request.GET)
		if form.is_valid():
			userObj = form.cleaned_data
			bvn_number = userObj['Bvn_number']
			email=userObj['EmailAddress']
			response=get_bvn_details(bvn_number)
			if response['status']!= 'success':
				messages=messages()
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


def creditcheck(request):
	context = {}
	template = 'user_dashboard/creditcheck.html'
	return render(request, template, context)


def loanhistory(request):
	context = {}
	template = 'user_dashboard/loanhistory.html'
	return render(request, template, context)


def repaymenthistory(request):
	context = {}
	template = 'user_dashboard/repaymenthistory.html'
	return render(request, template, context)

def repaymenthistory_doc(request):
	context = {}
	template = 'user_dashboard/repaymenthistory_doc.html'
	return render(request, template, context)