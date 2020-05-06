from django.contrib.auth import get_user_model
from rest_framework.authentication import TokenAuthentication
from .utils import get_token_model_auth


class TokenAuthentication(TokenAuthentication):
    """
    Simple token based authentication.

    Clients should authenticate by passing the token key in the "Authorization"
    HTTP header, prepended with the string "Token ".  For example:

        Authorization: Token 401f7ac837da42b97f613d789819ff93537bee6a
    """

    keyword = 'Token'
    model = None

    def get_model(self):
        User = get_user_model()
        self.model=get_token_model_auth(User)
        if self.model is not None:
            return self.model
        from rest_framework.authtoken.models import Token
        return Token

