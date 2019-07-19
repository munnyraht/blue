from django import forms
#from django.forms import ModelForm
from users.models  import  BluecreditUser
from backend.models import personalinfo
from django.contrib.auth.forms import UserCreationForm

# from backend.models import personalinformation

STATES = (
    ('', 'Choose...'),
    ('MG', 'Minas Gerais'),
    ('SP', 'Sao Paulo'),
    ('RJ', 'Rio de Janeiro')
)


class loginForm(forms.Form):
	email = forms.EmailField(required=True)
	password = forms.CharField(widget=forms.PasswordInput())

    
class RegisterForming(UserCreationForm):
    # ROLE = (('LoanMarketer','LoanMarketer'),('LoanMarketer','LoanMarketer'),)
    FirstName=forms.CharField(max_length=38, required=True)
    Surname = forms.CharField(max_length=38, required=True)
    Username = forms.CharField(max_length=38, required=True)
    Role=forms.CharField(max_length=38, required=True)
    EmailAddress=forms.EmailField(required=True)
    MobileNumber=forms.DecimalField(decimal_places=0, max_digits=11,required=True)
    password=forms.CharField(max_length=38,required = True, widget = forms.PasswordInput(attrs={'id':'password'}))
    # ConfirmPassword=forms.CharField(max_length=38,required=True,widget = forms.PasswordInput(attrs={'id':'confirmpassword'}))

    # class Meta:
    #     model = RegisterForm
    #     fields = ('Role', )
    #     widgets = {
    #       'secretdocs': Select(attrs={'LoanMarketer': 'LoanMarketer'}, {'LoanMarketer': 'LoanMarketer'}),

    #     }
 

class Bvn_number(forms.Form):
    EmailAddress=forms.EmailField(required=True)
    Bvn_Number= forms.CharField(max_length=11,required=True,)

class personalinfo(forms.Form):
    #MARRIAGESTATUS = (('1','Single'),('2','Married'),)

    MiddleName= forms.CharField(max_length=32)
    MobileNumber2=forms.IntegerField()
    DateOfBirth=forms.DateField(initial='mm/dd/yyy',)
    MaritalStatus=forms.CharField(max_length=38, required=True)
    PlaceOfBirth=forms.CharField(max_length=100)
    NumberOfDependent=forms.IntegerField(label='No Of Dependent')
    HomeAddress= forms.CharField()
    DateAtAddress=forms.DateField(initial='mm/dd/yyy',label='Date at Address ')

    # class Meta:

    #     model = personalinfo
    #     fields = [

    #     'MiddleName', 
    #     'MobileNumber2', 
    #     'DateOfBirth', 
    #     'MaritalStatus',
    #     'PlaceOfBirth', 
    #     'NumberOfDependent', 
    #     'HomeAddress', 
    #     'DateAtAddress',
    #     ]


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = BluecreditUser
        fields = (
            'username',
            'FirstName',
            'Surname',
            'Role',
            'EmailAddress',
            'MobileNumber',
            'active',            
        )

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.FirstName = self.cleaned_data['FirstName']
        user.Surname = self.cleaned_data['Surname']
        user.Role = self.cleaned_data['Role']
        user.EmailAddress = self.cleaned_data['EmailAddress']
        user.MobileNumber = self.cleaned_data['MobileNumber']
        user.active = self.cleaned_data['active']

        if commit:
            user.save()

        return user



