from django.db import models
from tutor.constants import GENDER_CHOICES, MEDIUM_OF_INSTRUCTION_CHOICES, CLASS_CHOICES, SUBJECT_CHOICES, TIME_CHOICES
from tutor.models import TutorModel
class SubjectChoice(models.Model):
    name = models.CharField(max_length=50, choices=SUBJECT_CHOICES)

    def __str__(self):
        return self.name

class Tuition(models.Model):
    title = models.CharField(max_length=100, default="Tuition For", help_text="Title of the tuition")
    subjects = models.ManyToManyField(SubjectChoice, related_name='tuitions', help_text="Subjects taught in this tuition")
    tuition_class = models.CharField(max_length=50, choices=CLASS_CHOICES, help_text="Class for which tuition is offered")
    availability = models.BooleanField(default=True, help_text="Availability status of the tuition")
    description = models.TextField(help_text="Detailed description of the tuition")
    medium = models.CharField(max_length=50, choices=MEDIUM_OF_INSTRUCTION_CHOICES, help_text="Medium of instruction")
    student_gender = models.CharField(max_length=50, choices=GENDER_CHOICES, help_text="Gender of students")
    preferred_tutor_gender = models.CharField(max_length=50, choices=GENDER_CHOICES, help_text="Preferred gender of tutor")
    tutoring_time = models.CharField(max_length=20, choices=TIME_CHOICES, help_text="Time for tutoring")
    number_of_students = models.PositiveIntegerField(default=1, help_text="Number of students")
    salary = models.DecimalField(max_digits=10, decimal_places=2, help_text="Salary offered per month")
    location=models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return self.title



STAR_CHOICES = [
    ( '⭐',        1 ),
    ( '⭐⭐',      2 ),
    ( '⭐⭐⭐' ,   3 ),
    ( '⭐⭐⭐⭐' , 4  ),
    ( '⭐⭐⭐⭐⭐',5  ),
]
class Review(models.Model):
    
    reviewer = models.ForeignKey(TutorModel, on_delete = models.CASCADE)
    comments = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    rating = models.CharField(max_length=5,choices = STAR_CHOICES)
    
def __str__(self):
    if self.reviewer.user:
        return f"Tutor Review: {self.reviewer.user.first_name}"
    else:
        return f"Tutor Review: No associated user"

