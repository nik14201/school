from django.conf.urls import url, include
from .serializers import ObjectModelViewSet
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'', ObjectModelViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]