from rest_framework.reverse import reverse
from rest_framework.views import APIView
from .serializers import *

from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import User
from rest_auth.registration.views import RegisterView
from django.conf import settings
from rest_auth.utils import jwt_encode
from rest_auth.app_settings import create_token
from allauth.account.utils import complete_signup
from allauth.account import app_settings as allauth_settings
from rest_auth.views import UserDetailsView, LoginView, LogoutView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response


class APIRootView(APIView):
    def get(self, request):
        context = {'request': ''}
        data = {
            'login': reverse('rest_login', request=request),
            'logout': reverse('rest_logout', request=request),
            'register': reverse('rest_register', request=request),
            'password-change': reverse('rest_password_change', request=request),
            'password-reset': reverse('rest_password_reset', request=request),
            'password-reset-confirm': reverse('rest_password_reset_confirm', request=request),
            'user-details': reverse('rest_user_details', request=request),
            #'profile': reverse('profile', request=request),
        }
        return Response(data)
    

# ViewSets define the view behavior.
class RegisterUserViewSet(RegisterView):
    serializer_class = RegisterUserSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        user = serializer.save()
        if getattr(settings, 'REST_USE_JWT', False):
            self.token = jwt_encode(user)
        else:
            create_token(self.token_model, user, serializer)
        complete_signup(self.request._request, user,
                        allauth_settings.EMAIL_VERIFICATION,
                        None)
        return user


# ViewSets define the view behavior.
class UserDetailsViewSet(UserDetailsView):
    serializer_class = UserDetailsSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self, *args, **kwargs):
        try:
            user = User.objects.get(email=self.request.user.email)
            return user
        except Exception as e:
            raise serializers.ValidationError({
                "type": "Error",
                "message": "Error User",
                "errors":[{
                    "name": "name",
                    "message": "Message",
                    }],
            })

    def get(self, request, format=None):
        element = self.get_object()
        serializer = UserDetailsSerializerGet(element)
        return Response(serializer.data)


class UserLoginViewSet(LoginView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny,)
    queryset=None

    def get_queryset(self):
        return User.objects.filter(email=self.request.user)

    def login(self):
        self.user = User.objects.get(email=self.serializer.validated_data['email'])

        if getattr(settings, 'REST_USE_JWT', False):
            self.token = jwt_encode(self.user)
        else:
            self.token = create_token(self.token_model, self.user,
                                      self.serializer)

        if getattr(settings, 'REST_SESSION_LOGIN', True):
            self.process_login()

    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data=self.request.data,
                                              context={'request': request})
        self.serializer.is_valid(raise_exception=True)

        email = request.POST.get('email', None)
        password = request.POST.get('password',None)
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError({
                "type": "authorization",
                "message": "Невозможно войти в систему с указанными учётными данными",
                "errors": [{
                    "name": "authorization",
                    "message": "Невозможно войти в систему с указанными учётными данными",
                }],
            })
        self.login()
        return self.get_response()

class UserLogoutViewSet(LogoutView):
    pass


class ObjectModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(username='admin')
    serializer_class = ObjectModelSerializer

    def create(self, request, *args, **kwargs):
        #serializer = self.get_serializer(data=request.data)
        #serializer.is_valid(raise_exception=True)
        #self.perform_create(serializer)
        #headers = self.get_success_headers(serializer.data)
        return Response(status=status.HTTP_200_OK)
