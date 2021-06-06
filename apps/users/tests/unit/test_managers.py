import pytest
from faker import Faker

from django.test import TestCase
from django.contrib.auth import get_user_model


@pytest.mark.django_db
class TestUserManager(TestCase):
    faker = Faker()

    def test_create_user_method(self):
        """Create method should save a new user with email and password"""
        password: str = self.faker.slug()
        new_user = get_user_model().objects.create_user(
            email=self.faker.email(),
            password=password
        )
        assert new_user.pk
        assert new_user.email
        assert new_user.check_password(password)

    def test_create_superuser_method(self):
        """Create method should create a superuser"""
        new_user = get_user_model().objects.create_superuser(
            email=self.faker.email(),
            password=self.faker.slug()
        )
        assert new_user.pk
        assert new_user.is_staff
        assert new_user.is_superuser
