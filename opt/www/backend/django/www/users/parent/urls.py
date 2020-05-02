from django.conf.urls import url, include
from django.urls import path
from .views import *
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'', ObjectModelViewSet)
#
# urlpatterns = [
# 	path('', APIRootView.as_view(), name='api-root'),
#     url(r'^login/$', UserLoginViewSet.as_view(), name='rest_login'),
#     url(r'^logout/$', UserLogoutViewSet.as_view(), name='rest_logout'),
#     url(r'^registration/$', RegisterUserViewSet.as_view(), name='rest_register'),
#     url(r'^user/$', UserDetailsViewSet.as_view(), name='rest_user_details'),
#     url(r'^profile/', include(router.urls), name='profile'),
#     path('auth/', include('rest_auth.urls')),
# ]