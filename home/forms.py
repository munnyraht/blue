from django import forms
from home.models import Contact
# from home.models import Personaldetails
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

# class PersonalDetailsForm(forms.ModelForm):
# 	class Meta:
# 		model = Personaldetails 
# 		exclude = ["timestamp",]
# 		widgets = {
# 			'message': forms.Textarea(attrs={'rows':4, 'cols':15}),
# 		}

# 	def __init__(self, *args, **kwargs):
# 		super(PersonalDetailsForm, self).__init__(*args, **kwargs)
# 		for field in self.fields:
# 			self.fields[field].widget.attrs.update({
# 		    'class': 'form-control'})
