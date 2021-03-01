from django.shortcuts import render
from .models import Flight
from .serializers import FlightSerializer
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class FlightViewSet(ModelViewSet):

    queryset = Flight.objects.all()
    serializer_class=FlightSerializer
