from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponse
# from django.core.mail import send_mail
from django.conf import settings
from backend.forms import loginForm,RegisterForm
from backend.models import user
from django import forms
from django.contrib import messages 
from passlib.hash import pbkdf2_sha256

def login(request):
	if request.method=='POST':
		form=loginForm(request.POST)
		if form.is_valid():
			obj=form.cleaned_data
			email=obj['EmailAddress']
			password=obj['Password']
			enc_password=pbkdf2_sha256.encrypt(password,rounds=12000,salt_size=32)
			if (user.objects.filter(EmailAddress=email).exists() and user.objects.filter(Password=enc_password).exists()):
				template = '../bluecredit'
				return redirect(template)
			else:
				error='LogIn details not found'
				context={ 'form':form,
						'error': error }
				return render(request, 'account/signin.html', context)
				#raise forms.ValidationError('Incorrect Email or password')
	else:
		form = loginForm()
		return render(request, 'account/signin.html', {'form' : form})


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
				if (password != confirmpassword):
					error = 'Password mismatch'
					context={ 'form':form,
							'error': error }
					return render(request, 'account/signup.html', context)
				enc_password=pbkdf2_sha256.encrypt(password,rounds=12000,salt_size=32)
				user.objects.create(FirstName=Firstname,Surname=Surname,Role=role, EmailAddress = email, MobileNumber=mobilenumber,Password=enc_password)
				# users = authenticate(EmailAddress = email, Password = password)
				# login(request)
				context = {
					'form':form
	              }
				template='../bluecredit'
				return redirect (template)
			else:
				error = 'Account already exists'
				context={ 'form':form,
						'error': error }
				return render(request, 'account/signup.html', context)
				#raise forms.ValidationError('Looks like a username with that email or password already exists')
	else:
		form = RegisterForm()
		context={ 'form':form}
		return render(request, 'account/signup.html', context)


def pending(request):
	context = {}
	template = 'account/pending.html'
	return render(request, template, context)

def index(request):
	context = {}
	template = 'dashboard/index.html'
	return render(request, template, context)


def results(request):
	context = {}
	template = 'dashboard/results.html'
	return render(request, template, context)


def personal(request):
	context = {}
	template = 'dashboard/personal.html'
	return render(request, template, context)

def loandetails(request):
	context = {}
	template = 'dashboard/loandetails.html'
	return render(request, template, context)
