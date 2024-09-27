from django.db import models

# Create your models here.
from django.db import models
from tutor.models import TutorModel
from tuition.models import Tuition

class Application(models.Model):
    tutor = models.ForeignKey(TutorModel, on_delete=models.CASCADE)
    tuition = models.ForeignKey(Tuition, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('applied', 'Applied'), ('accepted', 'Accepted')] ,default='applied')
    message = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.tutor.user.username} applied"