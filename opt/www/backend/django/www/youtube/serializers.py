from rest_framework import  serializers, viewsets
from .models import  ModelClassApp as ObjectModel
from rest_framework.response import Response

class ObjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectModel
        fields = '__all__'

class ObjectModelViewSet(viewsets.ModelViewSet):
    queryset = ObjectModel.objects.order_by('-id')
    serializer_class = ObjectModelSerializer
