from django.contrib import admin
from .models import *

# Register your models here

class TutorModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'gender', 'phone_number', 'location',]
    list_filter = ['gender',]
    search_fields = ['user__username', 'phone_number', 'location']
 


admin.site.register(StudentModel, TutorModelAdmin)