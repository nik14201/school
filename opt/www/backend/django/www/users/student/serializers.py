from rest_framework import serializers
from .models import TokenStudent

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = TokenStudent
        fields = ['key']