from django.db import models
from django.contrib.auth.models import User

class Extractions(models.Model):
    user_id = models.ForeignKey(User) 
    coffee_id = models.ForeignKey(Coffee)
    timestamp = models.DateTimeField()
    extraction_length = models.IntegerField()
    mass_in= models.DecimalField()
    mass_out = models.DecimalField()
    notes = models.CharField()
