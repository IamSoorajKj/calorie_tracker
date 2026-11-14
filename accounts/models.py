from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
  phone=models.CharField(max_length=15,unique=True)
  age=models.PositiveIntegerField()
  dob=models.DateField()
  height=models.FloatField()
  weight=models.FloatField()
