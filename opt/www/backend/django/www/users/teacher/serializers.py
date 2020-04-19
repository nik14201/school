from rest_framework import  serializers, viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()

class RegisterUserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['email', 'password']

    # def create(self, validated_data):
    #     user = super(RegisterUserSerializer, self).create(validated_data)
    #     user.set_password(validated_data['password'])
    #     user.is_staff = False
    #     user.username=validated_data['email']
    #     user.save()
    #     return user

class UserDetailsSerializerGet(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'email',  'avatar', 'first_name', 'last_name', 'title', 'phone', 
                    'skype', 'whatsapp', 'url_freelance', 'url_facebook', 'url_vk', 'telegram', 'url_telegram']

class UserDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['pk',  'avatar', 'first_name', 'last_name']

class UserLoginSerializer(serializers.HyperlinkedModelSerializer):
    email = serializers.EmailField(required=False, allow_blank=True)
    password = serializers.CharField(style={'input_type': 'password'})
    class Meta:
        model = User
        fields = ['email', 'password']


class ObjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

