from rest_framework import  serializers, viewsets
from .models import  MainModel
from rest_framework.response import Response

class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainModel
        fields = ['id', 'name', 'city', 'code']

class MainViewSet(viewsets.ModelViewSet):
    queryset = MainModel.objects.order_by('-id')[:1]
    serializer_class = MainSerializer