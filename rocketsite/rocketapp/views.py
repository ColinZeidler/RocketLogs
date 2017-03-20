from django.shortcuts import render
from django.contrib.auth.models import User, Group
from .models import Rocket, FlightLog
from .serializers import *
from rest_framework import viewsets, permissions

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class RocketViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Rocket.objects.all()
    serializer_class = RocketSerializer


class FlightViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = FlightLog.objects.all()
    serializer_class = FlightSerializer

    # TODO override create, so that it updates the flight count of the related rocket
