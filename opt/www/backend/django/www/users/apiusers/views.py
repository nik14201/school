from rest_framework import  viewsets
from rest_framework import status
from .serializers import *
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_auth.registration.views import RegisterView
from django.conf import settings
from rest_auth.utils import jwt_encode
from rest_auth.app_settings import create_token
from allauth.account.utils import complete_signup
from allauth.account import app_settings as allauth_settings
from rest_auth.views import UserDetailsView, LoginView, LogoutView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.contrib.auth import get_user_model
User = get_user_model()


class APIRootView(APIView):
    def get(self, request):
        context = {'request': ''}
        data = {
            'login': reverse('rest_login', request=request),
            'logout': reverse('rest_logout', request=request),
            'register': reverse('rest_register', request=request),
            #'password-change': reverse('rest_password_change', request=request),
            #'password-reset': reverse('rest_password_reset', request=request),
            #'password-reset-confirm': reverse('rest_password_reset_confirm', request=request),
            'user-details': reverse('rest_user_details', request=request),
            'isauth': reverse('isauth', request=request),
            #'profile': reverse('profile', request=request),
        }
        return Response(data)
    

# ViewSets define the view behavior.
class RegisterUserViewSet(RegisterView):
    serializer_class = RegisterUserSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        try:
            user = serializer.save()
            if getattr(settings, 'REST_USE_JWT', False):
                self.token = jwt_encode(user)
            else:
                create_token(self.token_model, user, serializer)
            complete_signup(self.request._request, user,
                            allauth_settings.EMAIL_VERIFICATION,
                            None)
        except Exception as e:
            pass
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
            try:
                self.token = create_token(self.token_model, self.user,
                                          self.serializer)
            except Exception as e:
                self.token=None
        if getattr(settings, 'REST_SESSION_LOGIN', True):
            self.process_login()

    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data=self.request.data,
                                              context={'request': request})
        self.serializer.is_valid(raise_exception=True)

        email = request.data.get('email', None)
        password = request.data.get('password',None)
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


class ObjectModelViewSet(APIView):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            serializers = ObjectModelSerializer(request.user)
            return Response(serializers.data)
        else:
            return Response({"authentificate": False})


class IsAuthentificateView(APIView):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response({"authentificate": True})
        else:
            return Response({"authentificate": False})