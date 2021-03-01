from django.shortcuts import render
# from django.contrib.auth.models import User
# from api.serializers import UserSerializer
# from rest_framework.viewsets import ModelViewSet
from django.views import View
# Create your views here.

# class UserViewSet(ModelViewSet):
#     queryset = User.object.all()
#     serializer_class=UserSerializer

class Index(View):
    def get(self, request, *args, **krgs ):
        return render(request, 'api/index.html')

    def post(self, request, *args, **krgs ):
        return render(request, 'api/index.html')
    
