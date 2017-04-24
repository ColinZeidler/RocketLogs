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
        fields = ('url', 'username', 'password', 'email', 'groups', 'rockets', 'flights')
        extra_kwargs = {
            'password': {'write_only': True},
            'rockets': {'read_only': True},
            'flights': {'read_only': True},
        }


class RocketSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

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
        extra_kwargs = {
            'flights': {'read_only': True},
        }


class FlightSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    rocketName = serializers.ReadOnlyField(source='rocket.name')

    class Meta:
        model = FlightLog
        fields = (
            'owner',
            'rocket',
            'rocketName',
            'launch_date',
            'notes_text',
            'motor',
            'delay',
            'altitude',
            'flight_result',
        )
