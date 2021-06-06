import pytest

from django.db.models import Model
from factory.django import DjangoModelFactory


@pytest.mark.django_db
class FactoryTestMixin(object):
    factory_class: DjangoModelFactory

    def test_create_new_object(self):
        """Make sure object is saved on db"""
        obj: Model = self.factory_class.create()
        assert obj.pk is not None

    def test_instance_new_object(self):
        """Create new instance of an object, but not saved on db"""
        instance = self.factory_class.build()
        assert instance is not None
        assert instance.pk is None
