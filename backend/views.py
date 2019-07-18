from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponse
# from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate
from backend.forms import loginForm,RegisterForm
from backend.models import user
from users.models import BluecreditUser
from django import forms
from django.contrib import messages 
from passlib.hash import pbkdf2_sha256

# def login(request):
# 	if request.method=='POST':
# 		form=loginForm(request.POST)
# 		if form.is_valid():
# 			obj=form.cleaned_data
# 			email=obj['email']
# 			password=obj['password']
# 			enc_password=pbkdf2_sha256.encrypt(password,rounds=12000,salt_size=32)
# 			if (BluecreditUser.objects.filter(email=email).exists() and BluecreditUser.objects.filter(password=enc_password).exists()):
# 				template = '../pending'

# 				return redirect(template)

# 			else:
# 				error='LogIn details not found'
# 				context={ 'form':form,
# 						'error': error }
# 				return render(request, 'account/signin.html', context)
# 				#raise forms.ValidationError('Incorrect Email or password')
# 	else:
# 		form = loginForm()
# 		return render(request, 'account/signin.html', {'form' : form})

def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			userObj = form.cleaned_data
			Firstname = userObj['FirstName']
			Surname=userObj['Surname']
			username=userObj['Username']
			role=userObj['Role']
			email =  userObj['EmailAddress']
			mobilenumber=userObj['MobileNumber']
			password =  userObj['password']
			confirmpassword=userObj['ConfirmPassword']

			if not (BluecreditUser.objects.filter(EmailAddress=email).exists()):
				if (password != confirmpassword):
					error = 'Password mismatch'
					context={ 'form':form,
							'error': error }
					return render(request, 'account/signup.html', context)
				enc_password=pbkdf2_sha256.encrypt(password,rounds=12000,salt_size=32)
				BluecreditUser.objects.create(username=username,FirstName=Firstname,Surname=Surname,Role=role, EmailAddress = email, MobileNumber=mobilenumber,password=enc_password)
				# users = authenticate(EmailAddress = email, Password = password)
				# login(request)
				context = {
					'form':form
	              }
				template='pending'
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


@login_required(login_url="../accounts/login")
def index(request):
	context = {}
	template = 'dashboard/index.html'
	return render(request, template, context)


@login_required(login_url="../accounts/login")
def results(request):
	context = {}
	template = 'dashboard/results.html'
	return render(request, template, context)


@login_required(login_url="../accounts/login")
def personal(request):
	context = {}
	template = 'dashboard/personal.html'
	return render(request, template, context)


@login_required(login_url="../accounts/login")
def loandetails(request):
	context = {}
	template = 'dashboard/loandetails.html'
	return render(request, template, context)
