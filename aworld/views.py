from django.shortcuts import  render 
from .models import *
from django.core.mail import message, send_mail
from django.views.generic import *

from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
class IndexView(TemplateView):
    template_name = 'aworld/index.html'

#===========================contact view===============================

def ContactView(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        comment = request.POST.get('comment')
        email = request.POST.get('email')
      
        
        send_mail(
            fname,
            comment,
            email,
            ['greenerhomes2020@gmail.com'],
            fail_silently=False,
            )
        return render(request,'aworld/email_sent.html',{'email':email})  
    return render(request,'aworld/contact.html',{})

#============================ABOUT VIEW===================================
class AboutView(TemplateView):
    template_name = 'aworld/about.html'  


#=====================================gALLERY vIEW===================================
class GalleryView(ListView):
    context_object_name = 'gallery'
    template_name = 'aworld/gallery.html'
    model = Gallery


class ServiceView(TemplateView):
    template_name = 'aworld/service.html' 