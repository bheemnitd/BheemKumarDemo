from django.contrib import admin
from django.urls import path, include
from api.views import Index
# from api.views import UserViewSet
# from rest_framework import routers
# router = routers.DefaultRouter()
# router.register('simplenight',UserViewSet)
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include(router.urls))
    path('',Index.as_view())
]
