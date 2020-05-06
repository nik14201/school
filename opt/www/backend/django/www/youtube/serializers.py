from rest_framework import  serializers, viewsets
from .models import  ModelClassApp

class ObjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelClassApp
        fields = '__all__'
