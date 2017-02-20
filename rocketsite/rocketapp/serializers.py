from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Rocket, FlightLog


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class RocketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rocket
        fields = (
            'owner',
            'name',
            'flight_count',
            'weight',
            'max_motor_diam',
            'max_altitude',
        )


class FlightSerializer(serializers.HyperlinkedModelSerializer):
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
