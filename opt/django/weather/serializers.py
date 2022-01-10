from rest_framework import  serializers, viewsets
from .models import  Weather as ObjectModel
from rest_framework.response import Response

class ObjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectModel 
        fields = '__all__'

