from apps.shared.tests.mixins import FactoryTestMixin
from apps.users.factories import UserFactory


class TestUserFactory(FactoryTestMixin):
    factory_class = UserFactory
    pass
