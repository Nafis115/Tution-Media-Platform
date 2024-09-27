from django.db import models
from tutor.constants import GENDER_CHOICES, MEDIUM_OF_INSTRUCTION_CHOICES, CLASS_CHOICES, SUBJECT_CHOICES, TIME_CHOICES,DAYS_OF_WEEK
from tutor.models import TutorModel
from student.models import StudentModel

class SubjectChoice(models.Model):
    name = models.CharField(max_length=50, choices=SUBJECT_CHOICES)

    def __str__(self):
        return self.name
    

    

class Tuition(models.Model):
    author=models.ForeignKey(StudentModel,on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default="Tuition For", help_text="Title of the tuition")
    subjects = models.ManyToManyField(SubjectChoice, related_name='tuitions', help_text="Subjects taught in this tuition")
    tuition_class = models.CharField(max_length=50, choices=CLASS_CHOICES, help_text="Class for which tuition is offered")
    description = models.TextField(help_text="Detailed description of the tuition")
    medium = models.CharField(max_length=50, choices=MEDIUM_OF_INSTRUCTION_CHOICES, help_text="Medium of instruction")
    student_gender = models.CharField(max_length=50, choices=GENDER_CHOICES, help_text="Gender of students")
    preferred_tutor_gender = models.CharField(max_length=50, choices=GENDER_CHOICES, help_text="Preferred gender of tutor")
    tutoring_time = models.CharField(max_length=20, choices=TIME_CHOICES, help_text="Time for tutoring")
    number_of_students = models.PositiveIntegerField(default=1, help_text="Number of students")
    salary = models.DecimalField(max_digits=10, decimal_places=2, help_text="Salary offered per month")
    location=models.CharField(max_length=100,null=True,blank=True)
    requirement=models.TextField(blank=True,null=True)
    created=models.DateField(auto_now_add=True,null=True,blank=True)
    
    def __str__(self):
        return self.title



class Review(models.Model):
    name = models.CharField(max_length=100)
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
