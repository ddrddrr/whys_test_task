import pytest
from pytest_factoryboy import register
from .misc import FACTORIES
from rest_framework.test import APIClient

for factory in FACTORIES:
	register(factory)


@pytest.fixture
def client():
	return APIClient()
