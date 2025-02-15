from django.db import models
from django.contrib.auth.models import User

class Cars(models.Model):
  model_lounge	= models.IntegerField()
  model_pop	= models.IntegerField()
  model_sport = models.IntegerField()
  previous_owners	= models.IntegerField()
  km = models.IntegerField()
  engine_power = models.IntegerField()
  age_in_days = models.IntegerField()
  date = models.DateField(auto_now=True)
  price = models.IntegerField()
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)