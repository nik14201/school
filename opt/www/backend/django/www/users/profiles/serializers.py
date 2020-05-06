from rest_framework import serializers
from .models import TokenProfile

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = TokenProfile
        fields = ['key']