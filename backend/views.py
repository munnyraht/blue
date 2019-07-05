from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
# from django.core.mail import send_mail
from django.conf import settings


def login(request):
	context = {}
	template = 'account/signin.html'
	return render(request, template, context)

def register(request):
	context = {}
	template = 'account/signup.html'
	return render(request, template, context)


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
