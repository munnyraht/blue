from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from home.models import HomeData
from home.models import Create
from home.models import Createnextofkin
from django.http import HttpResponse
# from django.core.mail import send_mail
from django.conf import settings



def home(request):
	homedata = HomeData.objects.all()
	context = {}
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

def verifybvn(request):
	context = {}
	template = 'bvnerror/verifybvn.html'
	return render(request, template, context)

def bvnaccepted(request):
	context = {}
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


