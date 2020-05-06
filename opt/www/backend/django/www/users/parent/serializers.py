from rest_framework import serializers
from .models import TokenParent

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = TokenParent
        fields = ['key']