from django.conf.urls import url, include
from django.urls import path
from .views import *

urlpatterns = [
	path('', APIRootView.as_view(), name='api-root'),
    path('login/', UserLoginViewSet.as_view(), name='rest_login'),
    path('logout/', UserLogoutViewSet.as_view(), name='rest_logout'),
    path('registration/', RegisterUserViewSet.as_view(), name='rest_register'),
    path('user/', UserDetailsViewSet.as_view(), name='rest_user_details'),
    path('profile/', ObjectModelViewSet.as_view(), name='profile'),
    #path('auth/', include('rest_auth.urls')),
    path('isauth/', IsAuthentificateView.as_view(), name='isauth'),
]