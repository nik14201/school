from rest_framework import serializers
from .models import TokenTeacher

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = TokenTeacher
        fields = ['key']