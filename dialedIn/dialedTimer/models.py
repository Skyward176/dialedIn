from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Coffee(models.Model):
    coffee_name = models.CharField(max_length=30)
    roaster_name = models.CharField(max_length=30)
    roast_level = models.CharField(max_length=30)


class Extraction(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    coffee_id = models.ForeignKey(Coffee, on_delete = models.CASCADE)
    timestamp = models.DateTimeField(default=datetime.now)
    extraction_length = models.IntegerField()
    mass_in= models.DecimalField(max_digits=5, decimal_places=3)
    mass_out = models.DecimalField(max_digits=5, decimal_places=3)
    notes = models.CharField(max_length=300)
