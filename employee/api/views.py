from django.shortcuts import render
from django.views import View
from .models import Employee
from rest_framework.viewsets import ModelViewSet
from .serializers import EmployeeSerializer

class EmployeeViewSet(ModelViewSet):
    
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
