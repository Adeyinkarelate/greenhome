from django.db import models
from django.urls import reverse
from cloudinary.models import CloudinaryField

# Create your models here.

class Gallery(models.Model):
    image = CloudinaryField('image')
    type_of_image = models.CharField(max_length=50 , null=True)
    content = models.CharField(max_length=200 , null=True)
    


    def __str__(self):  
        return self.type_of_image 