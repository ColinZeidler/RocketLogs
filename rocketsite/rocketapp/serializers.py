from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Rocket, FlightLog


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups', 'rockets')


class RocketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rocket
        fields = (
            'owner',
            'name',
            'flight_count',
            'weight',
            'max_motor_diam',
            'max_altitude',
            'flights',
        )


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightLog
        fields = (
            'rocket',
            'launch_date',
            'notes_text',
            'motor',
            'delay',
            'altitude',
            'flight_result',
        )
