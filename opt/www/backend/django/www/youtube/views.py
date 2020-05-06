from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from utils.authentication import TokenAuthentication
from rest_framework.response import Response
from .serializers import ObjectModelSerializer
from .models import ModelClassApp

class ObjectModelViewSet(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = ModelClassApp.objects.all()
    serializer_class = ObjectModelSerializer

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            elements = ModelClassApp.objects.all()
            print(elements)
            serializers=[]
            for element in elements:
                serializers.append(ObjectModelSerializer(element).data)
            return Response(serializers)
        else:
            return Response({"authentificate": False})
