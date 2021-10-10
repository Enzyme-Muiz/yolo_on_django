"""video_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from rest_framework.routers import DefaultRouter
import debug_toolbar

appname = "main"
router = DefaultRouter()
router.register(r'image_upload_point', views.Image_upload_ViewSet)

urlpatterns = [
    path('', views.homepage, name= "homepage"),
    path('video_uploads', views.uploads, name= "upload_videos"),
    path('yolo_function', views.yolo_good, name= "yolo_yolo"),
    #path('yolo_function', views.multiprocessing_exam, name= "yolo_yolo"),
    
    path('success', views.success, name = 'success'),
    path('detect_object', views.detect_object_object, name = 'detect_object_object'),
    path('func', views.apisample.as_view(), name= "api_sample"),
    path('function', views.FileUploadView.as_view(), name= "file_upload"),
    path('image_upload_point', include(router.urls)),
    #path('image_upload_point', views.Image_upload_ViewSet.as_view(), name= "f_upload"),
    path('detect_object_object_api', views.api_detect, name = 'detect_object_object_api_name'),

    path('__debug__/', include(debug_toolbar.urls)),
    
    
    


]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 