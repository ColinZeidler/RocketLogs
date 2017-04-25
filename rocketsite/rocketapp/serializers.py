from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Rocket, FlightLog


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'password', 'email', 'groups', 'rockets', 'flights')
        extra_kwargs = {
            'password': {'write_only': True},
            'rockets': {'read_only': True},
            'flights': {'read_only': True},
            'id': {'read_only': True},
        }


class RocketSerializer(serializers.ModelSerializer):
    owner_name = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Rocket
        fields = (
            'id',
            'owner',
            'owner_name',
            'name',
            'flight_count',
            'weight',
            'max_motor_diam',
            'max_altitude',
            'flights',
        )
        extra_kwargs = {
            'flights': {'read_only': True},
            'id': {'read_only': True},
            'owner': {'read_only': True},
        }


class FlightSerializer(serializers.ModelSerializer):
    owner_name = serializers.ReadOnlyField(source='owner.username')
    rocket_name = serializers.ReadOnlyField(source='rocket.name')

    class Meta:
        model = FlightLog
        fields = (
            'id',
            'owner',
            'owner_name',
            'rocket',
            'rocket_name',
            'launch_date',
            'notes_text',
            'motor',
            'delay',
            'altitude',
            'flight_result',
        )
        extra_kwargs = {
            'id': {'read_only': True},
            'owner': {'read_only': True},
        }
