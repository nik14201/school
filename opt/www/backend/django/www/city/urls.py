from django.conf.urls import url
from django.urls import path, include
from .serializers import MainViewSet
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'', MainViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]