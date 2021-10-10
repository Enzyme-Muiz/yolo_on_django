from django.contrib import admin
from .models import *

# Register your models here.

class video_uploadadmin(admin.ModelAdmin):
	list_display = ("video", "date")
	actions = None

class image_uploadadmin(admin.ModelAdmin):
	list_display = ("image", "date")
	actions = None


class api_sampleadmin(admin.ModelAdmin):
	list_display= ["model_input", "password"]
	actions= None




admin.site.register(videos_upload, video_uploadadmin)
admin.site.register(api_sample, api_sampleadmin)
admin.site.register(images_upload, image_uploadadmin)

