from django.db import models
from django.contrib.auth.models import User
from .constants import *
from student.models import StudentModel
from cloudinary.models import CloudinaryField

    
class TutorModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('image', default='placeholder_image_public_id')
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=15)
    designation=models.CharField(max_length=150,null=True,blank=True)
    subjects = models.CharField(max_length=100,null=True,blank=True)
    bio=models.TextField(null=True,blank=True)
    location = models.CharField(max_length=100)
    salary = models.PositiveIntegerField(null=True, blank=True)
    tutoring_experience = models.CharField(max_length=20)
    education=models.CharField(max_length=50,null=True,blank=True)
    medium_of_instruction = models.CharField(max_length=20, choices=MEDIUM_OF_INSTRUCTION_CHOICES)

 
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"



STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]
class TutorReview(models.Model):

    reviewer = models.ForeignKey(StudentModel, on_delete = models.CASCADE,related_name='teacher_review')
    tutor=models.ForeignKey(TutorModel,on_delete=models.CASCADE,related_name='tutor')
    review = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    rating = models.CharField(max_length=5,choices = STAR_CHOICES)
    
    
    def __str__(self):
        return f"tutor : {self.reviewer.user.first_name} review"