from django.contrib import admin
from .models import *

# Register your models here

class TutorModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'gender', 'phone_number', 'location', 'status']
    list_filter = ['gender', 'status']
    search_fields = ['user__username', 'phone_number', 'location']
 

class TutorEducationAdmin(admin.ModelAdmin):
    list_display = ['tutor', 'Exam_Name', 'passing_year', 'institution', 'Group', 'grade']
    list_filter = ['Exam_Name', 'passing_year', 'Group']
    search_fields = ['tutor__user__username', 'Exam_Name', 'institution']
    

class TutorReviewAdmin(admin.ModelAdmin):
    list_display = ['tutor', 'reviewer', 'rating', 'comment']
    list_filter = ['rating']
    search_fields = ['tutor__user__username', 'reviewer__username']
    

admin.site.register(TutorModel, TutorModelAdmin)
admin.site.register(TutorEducation, TutorEducationAdmin)
admin.site.register(TutorReview, TutorReviewAdmin)


