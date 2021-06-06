import factory

from django.contrib.auth import get_user_model

from factory.django import DjangoModelFactory


class UserFactory(DjangoModelFactory):
    class Meta:
        model = get_user_model()

    class Params:
        is_admin = factory.Trait(
            is_staff=True,
            is_superuser=True
        )

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    username = factory.Faker('word')
    email = factory.Faker('email')
    password = factory.PostGenerationMethodCall('set_password', 'default-password')
