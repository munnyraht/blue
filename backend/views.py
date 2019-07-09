from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
# from django.core.mail import send_mail
from django.conf import settings
from backend.forms import loginForm,RegisterForm
from backend.models import user
from django import forms

def login(request):
	if request.method=='POST':
		form=loginForm(request.POST)
		if form.is_valid():
			obj=form.cleaned_data
			email=obj['EmailAddress']
			password=obj['Password']
			if (user.objects.filter(EmailAddress=email).exists() and user.objects.filter(Password=password).exists()):
				context = {
					'form':form
				}
				template = 'dashboard/index.html'
				return render(request, template, context)
			else:
				raise forms.ValidationError('Incorrect Email or password')
	else:
		form = loginForm()
		return render(request, 'account/signup.html', {'form' : form})


def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			userObj = form.cleaned_data
			Firstname = userObj['FirstName']
			Surname=userObj['Surname']
			role=userObj['Role']
			email =  userObj['EmailAddress']
			mobilenumber=userObj['MobileNumber']
			password =  userObj['Password']
			confirmpassword=userObj['ConfirmPassword']
			if not (user.objects.filter(EmailAddress=email).exists()):
				user.objects.create(FirstName=Firstname,Surname=Surname,Role=role, EmailAddress = email, MobileNumber=mobilenumber,Password=password,ConfirmPassword=confirmpassword)
				# users = authenticate(EmailAddress = email, Password = password)
				# login(request)
				context = {
					'form':form
	              }
				template='dashboard/index.html'
				return render (request,template,context)
			else:
				raise forms.ValidationError('Looks like a username with that email or password already exists')
			
	else:
		form = RegisterForm()
		return render(request, 'account/signup.html', {'form' : form})


def pending(request):
	context = {}
	template = 'account/pending.html'
	return render(request, template, context)
@login_required
def index(request):
	users = user.objects.all()
	context = {}
	template = 'dashboard/index.html'
	return render(request, template,{'users':users} )

@login_required
def results(request):
	context = {}
	template = 'dashboard/results.html'
	return render(request, template, context)

@login_required
def personal(request):
	context = {}
	template = 'dashboard/personal.html'
	return render(request, template, context)

@login_required
def loandetails(request):
	context = {}
	template = 'dashboard/loandetails.html'
	return render(request, template, context)

@login_required
def salesreport(request):
	context = {}
	template = 'dashboard/salesreport.html'
	return render(request, template, context)
