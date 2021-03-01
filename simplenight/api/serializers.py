# from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

class FlightSerializer(ModelSerializer):

    class Meta:
        model=User
        fields=['username','password1','password2']

        