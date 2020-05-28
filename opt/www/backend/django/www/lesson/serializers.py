from rest_framework import  serializers, viewsets
from .models import  MainModel
from rest_framework.response import Response

class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainModel
        fields = ['name',  'code', 'subject', 'sclass',]

class MainViewSet(viewsets.ModelViewSet):
    queryset = MainModel.objects.order_by('-id')
    serializer_class = MainSerializer