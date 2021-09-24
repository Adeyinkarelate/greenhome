
from django.urls import path 
from .views import *

app_name = 'aworld'


urlpatterns = [
   path('',IndexView.as_view() , name='index'),
   path('contact/',ContactView, name="contact"),
   path('about/',AboutView.as_view() , name='about'),
   path('gallery/',GalleryView.as_view() , name='gallery'),
   path('service/',ServiceView.as_view() , name='service'),
   
]