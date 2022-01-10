from .views import ObjectModelViewSet
from django.urls import path

urlpatterns = [
    path('',ObjectModelViewSet.as_view()),
]