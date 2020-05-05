from rest_framework import  viewsets
from django.contrib.auth import (
    login as django_login,
    logout as django_logout
)
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from .serializers import *
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_auth.registration.views import RegisterView
from django.conf import settings
from rest_auth.utils import jwt_encode
from rest_auth.app_settings import JWTSerializer, create_token
from allauth.account.utils import complete_signup
from allauth.account import app_settings as allauth_settings
from rest_auth.views import UserDetailsView, LoginView, LogoutView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .utils import get_token_model, get_token_serializers


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
    token_serializer=None

    def get_response_data(self, user):
        if allauth_settings.EMAIL_VERIFICATION == \
                allauth_settings.EmailVerificationMethod.MANDATORY:
            return {"detail": _("Verification e-mail sent.")}

        if getattr(settings, 'REST_USE_JWT', False):
            data = {
                'user': user,
                'token': self.token
            }
            return JWTSerializer(data).data
        else:
            return self.token_serializer(user.auth_token).data


    def get_serializer_class(self):
        if not self.token_serializer is None:
            return self.token_serializer
        else:
            return super().get_serializer_class()

    def get_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
        except Exception as e:
            pass

        return Response(self.get_response_data(user),
                        status=status.HTTP_201_CREATED,
                        headers=headers)


    def perform_create(self, serializer):
        try:
            user = serializer.save()
            self.token_model = get_token_model(user)
            self.token_serializer = get_token_serializers(user)
            if getattr(settings, 'REST_USE_JWT', False):
                self.token = jwt_encode(user)
            else:
                try:
                    create_token(self.token_model, user, self.token_serializer)
                except:
                    pass
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


    def get_response_serializer(self):
        if getattr(settings, 'REST_USE_JWT', False):
            response_serializer = JWTSerializer
        else:
            response_serializer = self.token_serializer
        return response_serializer

    def login(self):
        self.user = User.objects.get(email=self.serializer.validated_data['email'])
        self.token_model = get_token_model(self.user)
        self.token_serializer = get_token_serializers(self.user)
        if getattr(settings, 'REST_USE_JWT', False):
            self.token = jwt_encode(self.user)
        else:
            try:
                self.token = create_token(self.token_model, self.user,
                                          self.token_serializer)
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
    def get(self, request, *args, **kwargs):
        if getattr(settings, 'ACCOUNT_LOGOUT_ON_GET', False):
            response = self.logout(request)
        else:
            response = self.http_method_not_allowed(request, *args, **kwargs)

        return self.finalize_response(request, response, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.logout(request)



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