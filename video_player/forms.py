from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import widgets


class VideoForm(forms.ModelForm):
	#def __init__(self, *args, **kargs):
	#	super(ImageForm, self).__init__(*args, **kargs)
	class Meta:
		model = videos_upload
		fields = ('video',)


class ImageForm(forms.ModelForm):
	#def __init__(self, *args, **kargs):
	#	super(ImageForm, self).__init__(*args, **kargs)
	class Meta:
		model = images_upload
		exclude = ('image',)

class image_for_yolo(forms.ModelForm):
	class Meta:
		model = api_sample
		fields = ('model_input',)
		exclude= ('string',)
	



