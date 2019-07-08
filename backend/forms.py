from django import forms
from .models  import user

class loginForm(forms.Form):
	EmailAddress = forms.CharField(
			required = True,
			label = 'Email',
			max_length = 32,
		)
	Password = forms.CharField(
			required = True,
			label = 'Password',
			max_length = 32,
			widget = forms.PasswordInput()
		)
class RegisterForm(forms.Form):
    FirstName=forms.CharField(max_length=38, required=True)
    Surname = forms.CharField(max_length=38, required=True)
    Role=forms.CharField(max_length=38,required=True)
    EmailAddress=forms.EmailField(required=True)
    MobileNumber=forms.DecimalField(decimal_places=0, max_digits=11,required=True)
    Password=forms.CharField(max_length=38,required=True)
    ConfirmPassword=forms.CharField(max_length=38,required=True)



