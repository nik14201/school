from rest_framework import  serializers, viewsets
from .models import  MainModel


class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainModel
        fields = ['id', 'teacher', 'student', 'homework']

class MainViewSet(viewsets.ModelViewSet):
    queryset = MainModel.objects.order_by('-id')[:1]
    serializer_class = MainSerializer