from django.contrib.auth import get_user_model

from rest_framework_simplejwt.tokens import AccessToken, RefreshToken


def get_access_token(user: get_user_model()) -> str:
    return AccessToken.for_user(user)


def get_refresh_token(user: get_user_model()) -> str:
    token_payload = RefreshToken.for_user(user)
    return str(token_payload)
