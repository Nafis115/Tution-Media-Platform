from django.db import models
from django.contrib.auth.models import User
from .constants import(
    GENDER_CHOICES,TUTORING_STATUS_CHOICES,MEDIUM_OF_INSTRUCTION_CHOICES,CLASS_CHOICES,SUBJECT_CHOICES,TIME_CHOICES,STAR_CHOICES
)

class ClassChoice(models.Model):
    name = models.CharField(max_length=50, choices=CLASS_CHOICES)

    def __str__(self):
        return self.name

class SubjectChoice(models.Model):
    name = models.CharField(max_length=50, choices=SUBJECT_CHOICES)
    def __str__(self):
        return self.name
    
class TimeChoice(models.Model):
    name = models.CharField(max_length=20, choices=TIME_CHOICES)

    def __str__(self):
        return self.name
    
    
    


class TutorModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='tutor/media/', default='default_image.png')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    tuition_district = models.CharField(max_length=100)
    minimum_salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=20, choices=TUTORING_STATUS_CHOICES, default='Available')
    days_per_week = models.IntegerField(default=5)
    tutoring_experience = models.CharField(max_length=20)
    extra_facilities = models.CharField(max_length=200)
    medium_of_instruction = models.CharField(max_length=20, choices=MEDIUM_OF_INSTRUCTION_CHOICES)
    preferred_class = models.ManyToManyField(ClassChoice)
    preferred_subjects = models.ManyToManyField(SubjectChoice)
    preferred_time = models.ManyToManyField(TimeChoice)
    preferred_area_to_teach = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.user.first_name}  {self.user.last_name}"

class TutorEducation(models.Model):
    tutor = models.ForeignKey(TutorModel, on_delete=models.CASCADE, related_name='education')
    Exam_Name = models.CharField(max_length=50)
    passing_year = models.IntegerField()
    institution = models.CharField(max_length=100)
    Group = models.CharField(max_length=50)
    grade = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.Group} - {self.tutor.user.username}"

class TutorReview(models.Model):
    tutor = models.ForeignKey(TutorModel, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.CharField(choices = STAR_CHOICES, max_length = 10)
    comment = models.TextField()

    def __str__(self):
        return f"Review by {self.reviewer.username} for {self.tutor.user.username}"

