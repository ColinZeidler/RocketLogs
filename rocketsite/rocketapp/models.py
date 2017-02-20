from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Rocket(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    flight_count = models.IntegerField()

    def __str__(self):
        return self.name



class FlightLog(models.Model):
    rocket = models.ForeignKey(Rocket, on_delete=models.CASCADE)
    launch_date = models.DateTimeField('date of launch')
    notes_text = models.TextField()
