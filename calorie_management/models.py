from django.db import models

from accounts.models import User

# Create your models here.
class FoodLog(models.Model):

  title=models.CharField(max_length=200,null=True)

  serving_size=models.CharField(max_length=200)

  calorie=models.FloatField(default=0.0)

  MEAL_CHOICHES=[
    ('breakfast','breakfast'),
    ('lunch','lunch'),
    ('dinner','dinner'),
    ('snacks','snacks')
  ]

  meal_type=models.CharField(max_length=200,choices=MEAL_CHOICHES,default='breakfast')

  owner=models.ForeignKey(User,on_delete=models.CASCADE)

  food_image=models.ImageField(upload_to='foods',null=True)
  
  created_at=models.DateTimeField(auto_now_add=True)
  