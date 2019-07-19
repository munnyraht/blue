from django import forms
from home.models import Contact
from home.models import Createnextofkin
from home.models import Acknowledgement
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
        
