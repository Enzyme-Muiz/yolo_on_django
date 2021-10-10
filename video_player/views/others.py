from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import HttpResponse
from ..forms import *
from ..models import *
from django.views.decorators.cache import cache_page
import cv2
from subprocess import run, PIPE, Popen
import sys
from multiprocessing import Pool
from django.core import serializers as core_serializers

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import serializers, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
#from rest_framework.decorators import MultiPartParser, FormParser
from rest_framework.parsers import JSONParser
from django.conf import settings
import uuid
import json

# Create your views here.
@cache_page(60 * 10)
def homepage(request):
    return render(request, 'main/home.html')
    #return HttpResponse("<h2>hello world</h2>")


def detect_object_object(request):
    #first_queryset = api_sample.objects.all().values("model_input").last()
    #image_data1= "media/"+ first_queryset['model_input']
    image_data1= "media/images/"+ request.COOKIES['picture_from_me']
    #with open(image_data1, mode='rb') as f:
    #    image_data = f.read()
        #image_data3 = image_data.encode(encoding="ascii")
    with open("src.jpg", mode='w+b') as f:
        
        #open("src.jpg", "rb") as instream:
        out= run([sys.executable, "C://Users//rajim//Desktop//video_django2//video_django//tutorial.py", image_data1], shell= True, stdout=f)
        #out.wait()

    #out= run([sys.executable, "C://Users//rajim//Desktop//video_django2//video_django//tutorial.py", image_data1], shell= True, stdout=PIPE)
    #print(out)
    #with open(out, mode='rb') as f:
    #    image_data = f.read()
    #ldh= out.stdout
    #print( "My name is {0}, I'm {1}".format("John",ldh))
    with open("big.jpg", "rb") as instream:
        image_data = instream.read()
    return HttpResponse(image_data, content_type="image/jpg")


#buf = io.BytesIO()
#	pyplot.savefig(buf, format='jpg')
#    sys.stdout.buffer.write(buf.getvalue())
@cache_page(60 * 10)
def uploads(request):
    if request.method == 'POST': 
        form = VideoForm(request.POST, request.FILES)
        form1 = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            fs= form.save(commit=False)
            fs.user= request.user 
            fs.save()
            return redirect('success') 
    else:
        form = VideoForm() 
        form1 = ImageForm()
        #just trying to print sessionID to my shell
        session_key1 = request.session.session_key
        print(session_key1)


    return render(request, 'main/video_uploading.html', {"form": form, "form1": form1})

def yolo_good(request):
    if request.method == 'POST': 
        form = image_for_yolo(request.POST, request.FILES)
        #request.session['video_file'] = video_upload.hashed_video_file_name
        if form.is_valid():
            username= form.cleaned_data.get("model_input")
            #request.session['file_name'] = core_serializers.serialize('json', username)
            #request.session['fav_color'] = 'blue'
            #print(username)
            fs= form.save(commit=False)
            fs.string = str(uuid.uuid4())+".jpg"
            fs.save()
           
            response= redirect('detect_object_object') 
            response.set_cookie('picture_from_me', fs.string) 
            return response
    else:
        form = image_for_yolo() 
       
    return render(request, 'main/image_yolo.html', {"form": form})

#implementing multiprocessing
def multiprocessing_exam(request):
    pool = Pool(5)
    #numbers = [1, 3, 5]
    results = pool.map(yolo_good)
    return HttpResponse(results)

def success(request):  
    if not request.COOKIES.get('color'):
        response = HttpResponse("Cookie Set")
        response.set_cookie('color', 'blue')
        return response
    else:
        response= HttpResponse("Your favorite color is {0}".format(request.COOKIES['color']))
        response.set_cookie('color', 'blue')
        return response

    #return HttpResponse('successfully uploaded')

class IncredibleInputSerializer(serializers.Serializer):
    model_input = serializers.CharField()

class apisample(APIView):

    def get(self, request):
        serializer = IncredibleInputSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        # Get the model input
        data = serializer.validated_data
        model_input = data["model_input"]

        # Perform the complex calculations
        complex_result = model_input + "xyz"

        # Return it in your custom format
        return Response({
            "complex_result": complex_result,
        })
    
    def post(self, request):
        serializer = IncredibleInputSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.validated_data
            new= data["model_input"]
            api_sample.objects.create(model_input= new)
            #serializer.save()
            return Response(serializer.data, status= 201)
        return Response(serializer.errors, status=400)
    



# i want to use this API endpoint to upload picture to a database:


def api_detect(request):
   
    image_data1= "media"+ request.COOKIES['picture_from_me']
    with open("src.jpg", mode='w+b') as f:
        out= run([sys.executable, "C://Users//rajim//Desktop//video_django2//video_django//tutorial.py", image_data1], shell= True, stdout=f)
    with open("remodelled{}".format( request.COOKIES['picture_from_me']), "rb") as instream:
        image_data = instream.read()
    return HttpResponse(image_data, content_type="image/jpg")   





class FileUploadView(APIView):
    parser_classes = (FileUploadParser,)

    def put(self, request, filename, format="jpg"):
        file_obj = request.FILES['file']
        # do some stuff with uploaded file
        return Response(status=204)




class PhotoInputSerializer(serializers.ModelSerializer):
    #model_input = serializers.ImageField(use_url=True)
    #string = serializers.CharField(max_length= 256)
    #image_url= serializers.SerializerMethodField
    #def get_image(self, instance):
    #    return instance.image.url if instance.image else ''
    class Meta:
        model = api_sample
        fields = ('model_input',) 
        #exclude= ('string',)
#developing an API that receives the image an process it.  
#class Image_upload_ViewSet(viewsets.ModelViewSet):

class Image_upload_ViewSet(viewsets.ModelViewSet):
    queryset = api_sample.objects.all()
    serializer_class = PhotoInputSerializer
    def perform_create(self, serializer):
        serializer.save(string = str(uuid.uuid4())+".jpg")

 


'''
class Image_upload_ViewSet(APIView):
    parser_classes = (MultiPartParser, FormParser, )
    #parser_classes = [JSONParser]

    #permission_classes = [IsAuthenticated]
    #queryset = api_sample.objects.all()
    #serializer_class = PhotoInputSerializer()

    def post(self, request, *args, **kwargs):
        #file = request.data['model_input']
        #print("hello")
        #image = api_sample.objects.create(model_input=file, string= "images/"+str(uuid.uuid4())+".jpg")
        #queryset = api_sample.objects.all()
        #serializer = PhotoInputSerializer(queryset, many=True, context={"request":request})
        serializer_class = PhotoInputSerializer(data=request.data)
        if serializer_class.is_valid():
            #request.session['file_name'] = core_serializers.serialize('json', username)
            #request.session['fav_color'] = 'blue'
            #print(username)
        #    serializer_class.string= "images/"+str(uuid.uuid4())+".jpg"
            #serializer_class.save()
            serializer_class.save(string = str(uuid.uuid4())+".jpg")
            #fs.string = str(uuid.uuid4())+".jpg"
            #fs.save()
        #print(file)
        return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)
        
        
        
        #response= redirect('detect_object_object_api_name') 
        #response.set_cookie('picture_from_me', fs.string) 
        #return response
        #return Response({
        #    "complex_result": ,
        #})
'''