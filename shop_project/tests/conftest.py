import pytest
from pytest_factoryboy import register
from .misc import FACTORIES
from rest_framework.test import APIClient
from django.apps import apps
import importlib

for factory in FACTORIES:
	register(factory)


@pytest.fixture
def client():
	return APIClient()
