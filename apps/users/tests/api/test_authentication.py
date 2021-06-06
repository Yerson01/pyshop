from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from apps.users.factories import UserFactory
from apps.shared.utils.auth import get_refresh_token


class TestLogin(APITestCase):
    create_token_url = reverse('users:jwt-create')
    refresh_token_url = reverse('users:jwt-refresh')

    def setUp(self) -> None:
        self.password: str = 'test-password'
        self.user = UserFactory(password=self.password)
        self.client.force_authenticate(self.user)

    def test_create_token(self):
        """Create token should be successful"""
        payload = {'password': self.password, 'email': self.user.email}
        res = self.client.post(self.create_token_url, payload)
        assert res.status_code == status.HTTP_200_OK
        assert 'access' in res.data
        assert 'refresh' in res.data

    def test_create_token_unauthorized(self):
        """Response should be unauthorized with invalid credentials"""
        payload = {'email': 'invalid@email.com', 'password': 'invalid'}
        res = self.client.post(self.create_token_url, payload)
        assert res.status_code == status.HTTP_401_UNAUTHORIZED

    def test_refresh_token(self):
        """Refresh token should be successful with valid refresh token"""
        refresh_token: str = get_refresh_token(self.user)
        payload = {'refresh': refresh_token}
        res = self.client.post(self.refresh_token_url, payload)
        assert res.status_code == status.HTTP_200_OK
        assert 'access' in res.data

    def test_refresh_token_unauthorized(self):
        """Refresh token with invalid refresh token is unauthorized"""
        payload = {'refresh': 'invalid-token'}
        res = self.client.post(self.refresh_token_url, payload)
        assert res.status_code == status.HTTP_401_UNAUTHORIZED
