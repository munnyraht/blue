from django import forms
from .models  import user

STATES = (
    ('', 'Choose...'),
    ('MG', 'Minas Gerais'),
    ('SP', 'Sao Paulo'),
    ('RJ', 'Rio de Janeiro')
)

class loginForm(forms.Form):
	EmailAddress = forms.EmailField(required=True)
	Password = forms.CharField(widget=forms.PasswordInput())



    
class RegisterForm(forms.Form):
    FirstName=forms.CharField(max_length=38, required=True)
    Surname = forms.CharField(max_length=38, required=True)
    Role=forms.CharField(max_length=38,required=True)
    EmailAddress=forms.EmailField(required=True)
    MobileNumber=forms.DecimalField(decimal_places=0, max_digits=11,required=True)
    Password=forms.CharField(max_length=38,required = True,widget = forms.PasswordInput())
    ConfirmPassword=forms.CharField(max_length=38,required=True,widget = forms.PasswordInput())

class Bvn_number(forms.Form):
    Email=forms.EmailField(required=True)
    Bvn_Number= forms.DecimalField(decimal_places=0, max_digits=11,required=True)




