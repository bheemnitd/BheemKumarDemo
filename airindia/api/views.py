from django.shortcuts import render
from .models import Flight
from .serializers import FlightSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class FlightViewSet(ModelViewSet):

    queryset = Flight.objects.all()
    serializer_class=FlightSerializer
    authentication_class=[JWTAuthentication]
    permission_class=[IsAuthenticated]
