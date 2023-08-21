import pytest
from pytest_factoryboy import register

from rest_framework.test import APIClient

from .model_factories import attribute_factory as af, product_factory as pf, image_factory as imgf

FACTORIES = {
	af.AttributeNameFactory,
	af.AttributeValueFactory,
	af.AttributeFactory,
	imgf.ImageFactory,
	pf.ProductFactory,
	pf.ProductAttributesFactory,
	pf.ProductImageFactory,
	pf.CatalogFactory,
}

for f in FACTORIES:
	register(f)


@pytest.fixture
def client():
	return APIClient()
