from django import forms
from home.models import Contact
from home.models import Createnextofkin
from home.models import Acknowledgement
from home.models import Personaldetails
from home.models import personalinfomodel
from backend.models import personalinfomodel
from django.contrib import messages

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		exclude = ["timestamp", ]
		widgets = {
			'message': forms.Textarea(attrs={'rows':4, 'cols':15}),
		}

	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs.update({
		    'class': 'form-control'})

class Createnextofkinform(forms.ModelForm):
	class Meta:
		model = Createnextofkin 
		exclude = ["timestamp",]
		widgets = {
			'message': forms.Textarea(attrs={'rows':4, 'cols':15}),
		}

	# def __init__(self, *args, **kwargs):
	# 	super(Createnextofkin, self).__init__(*args, **kwargs)
	# 	for field in self.fields:
	# 		self.fields[field].widget.attrs.update({
	# 	    'class': 'form-control'})


class Acknowledgement(forms.ModelForm):
    class Meta:
        model = Acknowledgement
        fields = ('terms_and_conditions', 'how_you_heard_about_us',  'signature', )
        

class Personal(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = personalinfomodel
        fields = (
        'MiddleName', 
        'MobileNumber2', 
        'DateOfBirth', 
        'MaritalStatus',
        'PlaceOfBirth', 
        'NumberOfDependent', 
        'HomeAddress', 
        'DateAtAddress',           
        )

    def save(self, commit=True):
        user = super(Personal, self).save(commit=False)
        user.MiddleName = self.cleaned_data['MiddleName']
        user.MobileNumber2 = self.cleaned_data['MobileNumber2']
        user.DateOfBirth = self.cleaned_data['DateOfBirth']
        user.MaritalStatus = self.cleaned_data['MaritalStatus']
        user.PlaceOfBirth = self.cleaned_data['PlaceOfBirth']
        user.NumberOfDependent = self.cleaned_data['NumberOfDependent']
        user.HomeAddress = self.cleaned_data['HomeAddress']
        user.DateAtAddress = self.cleaned_data['DateAtAddress']
        

        if commit:
            user.save()

        return user
