from django.db import models

# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=100, blank=False)
    age=models.IntegerField(blank=False)
    city=models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name