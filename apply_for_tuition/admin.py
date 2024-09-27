# admin.py

from django.contrib import admin
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import Application  
from tutor.models import TutorModel  
from tuition.models import Tuition  

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['tutor_name',  'status']  

    def tutor_name(self, obj):
        return obj.tutor.user.first_name   

   

    def save_model(self, request, obj, form, change):
        if not obj.id:  
            obj.tutor = request.user.tutormodel  
            obj.save()
        else:
            obj.save()

        if obj.status == "accepted":
            email_subject = "Your Tuition Application Accepted"
            email_body = render_to_string('admin_email.html', {'user': obj.tutor.user, 'tuition': obj.tuition})
            
            email = EmailMultiAlternatives(email_subject, '', to=[obj.tutor.user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()

admin.site.register(Application, ApplicationAdmin)
