from django.contrib import admin
from .models import Tuition,SubjectChoice,Review
# Register your models here.
class TuitionAdmin(admin.ModelAdmin):
    list_display = ('title', 'tuition_class', 'availability', 'medium', 'student_gender', 'preferred_tutor_gender', 'number_of_students', 'salary')
    list_filter = ('tuition_class', 'availability', 'medium', 'student_gender', 'preferred_tutor_gender')
    search_fields = ('title', 'description')


admin.site.register(Tuition)
admin.site.register(SubjectChoice)
admin.site.register(Review)

