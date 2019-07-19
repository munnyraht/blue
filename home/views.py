from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from home.models import HomeData
from home.models import Create
from home.models import Contact
from home.models import Createnextofkin
from home.models import EmploymentDetails
from django.http import HttpResponse
# from django.core.mail import send_mail
from django.conf import settings
from backend.models import  bvn_details,personalinfomodel
from backend import views 
from users.models import BluecreditUser
from backend.forms import Bvn_number,personalinfo 
from home.forms import Createnextofkinform
from home.forms import Personal
from home.functions import get_bvn_details
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from home.models import Acknowledgement
from home.forms import Acknowledgement


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

def paymentinfo(request,email='godfredakpan@gmail.com'):
	user_details = BluecreditUser.objects.get(email=email)
	if request.method=='POST':
		form=Personal(request.POST)
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
			# email = email = BluecreditUser.objects.get(EmailAddress=email)
			# user_id = user_id = request.BluecreditUser(id)
			personalinfomodel.objects.create(MiddleName=MiddleName,MobileNumber2=MobileNumber2,DateOfBirth=DateOfBirth,MaritalStatus=MaritalStatus,PlaceOfBirth=PlaceOfBirth,NumberOfDependent=NumberOfDependent,DateAtAddress=DateAtAddress,HomeAddress=HomeAddress)
			template = 'paymentinfo/nextofkin.html'
			return render(request, template, {})
			#return redirect(template)

	else:
		form=Personal()
		# context = {'user_details': user_details, 'form': form}
		# template = 'paymentinfo/paymentinfo.html'
	return render(request, 'paymentinfo/paymentinfo.html', {'user_details': user_details, 'form': form})

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
	context = {'nextofkindata': nextofkindata}
	template = 'paymentinfo/nextofkin.html'
	return render(request, template, context )


def bvnerror(request):
	context = {}
	template = 'bvnerror/bvnerror.html'
	return render(request, template, context)


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
				return render(request,'bvnerror/verifybvn.html',{'form':form})
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
				user_id=BluecreditUser.objects.get(EmailAddress=email)
				bvn_details.objects.create(user_id=user_id,email=email,bvn=bvn,first_name=first_name,last_name=last_name,middle_name=middle_name,date_of_birth = date_of_birth, phone_number=phone_number, registration_date=registration_date,enrollment_bank=enrollment_bank, enrollment_branch=enrollment_branch)
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
    	# user_id = request.BluecreditUser(id)

    	)

    instance=createnextofkin.save()
    # instance=createnextofkin.save()
    # instance.user_id = request.BluecreditUser
    # instance()
    return redirect('paymentinfo/employmentinfo.html')

def createemploymentinfo(request):
	# if (request.method=='POST'):
	    createemploymentinfo = EmploymentDetails(
	    	Bankname=request.POST['bankname'],
	    	Existing_bank_account_number=request.POST['accountnumber'],
	    	Highest_level_of_education=request.POST['highestlevelofeducation'],
	    	Employment_status=request.POST['employmentstatus'],
	    	Current_employer=request.POST['currentemployer'],
	    	Employers_address_and_department=request.POST['employeraddress'],
	    	Landmark_closest_to_address=request.POST['landmark'],
	    	Income=request.POST['income'],
	    	Net_monthly_income_with_tax=request.POST['netincome'],
	    	)

	    createemploymentinfo.save()
	    return redirect('acknowledgement/acknowledgement.html')

	# else:
	# 	context = {}
	# 	template = 'paymentinfo/employmentinfo.html'
	# 	return render(request, template, context)

def creditcheck(request):
	context = {}
	template = 'user_dashboard/creditcheck.html'
	return render(request, template, context)

def personaldetails(request):
	context = {}
	template = 'paymentinfo/paymentinfo.html'
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

def acknowledgement_form_upload(request):
    if request.method == 'POST':
        form = Acknowledgement(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit='False')
            instance.user_id = request.user
            instance.save()
            return redirect('acknowledgement/acknowledgement.html')
    else:
        form = Acknowledgement()
    return render(request, 'acknowledgement/acknowledgement.html', {
        'form': form
    })

# def paymentinfo(request):
#     if request.method =='POST':
#         form = Personal(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('paymentinfo/nextofkin.html')
#     else:
#         form = Personal()

#         args = {'form': form}
#     return render(request, 'paymentinfo/paymentinfo.html', args)