from rest_framework import  serializers, viewsets
from .models import  MainModel
from rest_framework.response import Response
from utils.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView

class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainModel
        fields = ['name',  'code', 'subject', 'sclass',]


class MainViewSet(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    parser_classes = [MultiPartParser,]

    def patch(self, request,  *args, **kwargs):
        if request.user.is_authenticated:
            serializer = MainSerializer(request.user, data=request.data,  partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"authentificate": False})

    def post(self, request,  *args, **kwargs):
        if request.user.is_authenticated:
            serializer = MainSerializer(request.user, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"authentificate": False})

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            queryset = MainModel.objects.order_by('-id').filter(_lesson___sclass=request.user._sclass)
            serializers = [MainSerializer(q).data for q in queryset]
            return Response(serializers)
        else:
            return Response({"authentificate": False})


class MainViewSetEdit(MainViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    parser_classes = [MultiPartParser, ]

    def patch(self, request, pk,  *args, **kwargs):
        print("Homework Edit")
        if request.user.is_authenticated:
            queryset = MainModel.objects.order_by('-id').filter(_lesson___sclass=request.user._sclass, id=pk)[0]
            print(queryset)
            serializer = MainSerializer(queryset, data=request.data,  partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            print(serializer)
            return Response(serializer.data)
        else:
            return Response({"authentificate": False})

    def get(self, request, pk, *args, **kwargs):
        if request.user.is_authenticated:
            queryset = MainModel.objects.order_by('-id').filter(_lesson___sclass=request.user._sclass, id=pk)
            serializers = [MainSerializer(q).data for q in queryset]
            return Response(serializers)
        else:
            return Response({"authentificate": False})