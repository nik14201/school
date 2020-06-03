from .serializers import MainViewSet
from django.urls import path

urlpatterns = [
    path('', MainViewSet.as_view(), name='homework'),
]