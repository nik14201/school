from .serializers import MainViewSet, MainViewSetEdit
from django.urls import path

urlpatterns = [
    path('', MainViewSet.as_view(), name='lesson'),
    path('<str:pk>', MainViewSetEdit.as_view(), name='lesson'),
]