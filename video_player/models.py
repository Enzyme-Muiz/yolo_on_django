from django.db import models
#plan to hash a field
from django.contrib.auth.hashers import make_password
import random


# Create your models here.
class tutorial(models.Model):
    tutorial_title=  models.CharField(max_length= 200)
    tutorial_content = models.TextField()
    tutorial_published= models.DateTimeField("date_published")
    def __str__(self):
        return self.tutorial_title

class videos_upload(models.Model):
    video = models.FileField(upload_to='videos/')
    date= models.DateTimeField(auto_now_add= True)
    def __str__(self):
        return self.name
        
    
    
class images_upload(models.Model):
    image = models.ImageField(upload_to='images/')
    date= models.DateTimeField(auto_now_add= True)
    def __str__(self):
        return self.name
    

class api_sample(models.Model):
    model_input = models.ImageField(upload_to='images/')
    date= models.DateTimeField(auto_now_add= True)
    string = models.CharField(max_length= 256)
    #password = make_password(str(model_input)+ str(date))
    password = models.CharField(max_length= 256)
    def __str__(self):
        return self.model_input 
    def save(self, **kwargs):
        password1 = make_password(str(self.model_input)+ str(self.date))
        #print(str(self.model_input))
        self.password =password1

        print(password1)
        #randomNum = random.randint(10000,90000)
        #new_name = str(randomNum) + ".txt"
        self.model_input.name = self.string
        super().save(**kwargs)
    

    