from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

from doctor.models import Doctor


# Create your models here.

class Appointment(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField()
    created_at = models.DateField(default=datetime.today())
    patient = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, default=None)