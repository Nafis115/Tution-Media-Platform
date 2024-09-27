from django.db import models
from django.contrib.auth.models import User
from tutor.constants import *
# Create your models here.


class StudentModel(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='student')
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
  
    
    
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"