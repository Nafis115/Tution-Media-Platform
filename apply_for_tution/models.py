from django.db import models

# Create your models here.
from django.db import models
from tutor.models import TutorModel
from tution.models import Tuition

class Application(models.Model):
    tutor = models.ForeignKey(TutorModel, on_delete=models.CASCADE)
    tuition = models.ForeignKey(Tuition, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('applied', 'Applied'), ('accepted', 'Accepted')])

    def __str__(self):
        return f"{self.tutor.user.username} applied"