from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.


class Rocket(models.Model):
    owner = models.ForeignKey(
        User,
        related_name='rockets',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=150)
    flight_count = models.IntegerField(default=0)
    weight = models.FloatField(default=0)
    max_motor_diam = models.IntegerField(default=0)
    max_altitude = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class FlightLog(models.Model):
    rocket = models.ForeignKey(
        Rocket,
        related_name='flights',
        on_delete=models.CASCADE
    )
    launch_date = models.DateField(default=date.today)
    notes_text = models.TextField(default="")
    motor = models.CharField(max_length=100, default="")
    delay = models.PositiveSmallIntegerField(default=0)
    altitude = models.PositiveIntegerField(default=0)
    
    # result
    SUCCESS ='SS'
    NO_FIRE = 'NF'
    LATE_DEPLOY = 'LD'
    NO_DEPLOY = 'ND'
    CATO = 'CA'
    FLIGHT_RESULT_CHOICES = (
        (SUCCESS, 'Success'),
        (NO_FIRE, 'No Fire'),
        (LATE_DEPLOY, 'Late Deploy'),
        (NO_DEPLOY, 'No Deploy'),
        (CATO, 'CATO'),
    )
    flight_result = models.CharField(
        max_length=2,
        choices=FLIGHT_RESULT_CHOICES,
        default=NO_FIRE,
    )

