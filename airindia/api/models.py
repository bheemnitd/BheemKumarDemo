from django.db import models

# Create your models here.
class Flight(models.Model):

    flight_name=models.CharField(max_length=20, blank=False)
    flight_id = models.CharField(max_length=10, unique=True)
    departure_time = models.DateTimeField(blank=False)
    arrival_time = models.DateTimeField(blank=False)
    fare = models.IntegerField(blank=False)
    source=models.CharField(max_length=50,blank=False)
    destination=models.CharField(max_length=50, blank=False)
    
    def __str__(self):
        return self.flight_name