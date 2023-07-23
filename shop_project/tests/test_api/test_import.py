import pytest
from ..misc import IMPORT_ENDPOINT, TEST_DATA
import json

from attributes.serializers import (
	AttributeNameSerializer,
	AttributeValueSerializer,
	AttributeSerializer
)
from products.serializers import (
	ProductSerializer,
	ProductAttributesSerializer,
	ProductImageSerializer,
	CatalogSerializer
)
from images.serializers import ImageSerializer

pytestmark = pytest.mark.django_db


def is_created(client, model_name, data):
	response = client.post(IMPORT_ENDPOINT, data={model_name: data}, format='json')
	assert response.status_code == 201


class TestImport:
	def test_import_task_data_json(self, client):
		with open(TEST_DATA, mode='r', encoding='utf-8') as td:
			test_data = json.load(td)
			for payload in test_data:
				response = client.post(IMPORT_ENDPOINT, data=payload, format='json')
				if response.status_code != 201:
					print(payload, "--------------------------", response.json())
				assert response.status_code == 201

	def test_import_attribute_name(self, client, attribute_name):
		serializer = AttributeNameSerializer(attribute_name)
		is_created(client, attribute_name._meta.model.__name__, serializer.data)

	def test_import_product(self, client, product):
		serializer = ProductSerializer(product)
		is_created(client, product._meta.model.__name__, serializer.data)

	def test_import_product_attributes(self, client, product_attributes):
		serializer = ProductAttributesSerializer(product_attributes)
		is_created(client, product_attributes._meta.model.__name__, serializer.data)

	def test_import_product_image(self, client, product_image):
		serializer = ProductImageSerializer(product_image)
		is_created(client, product_image._meta.model.__name__, serializer.data)

	def test_import_catalog(self, client, catalog):
		serializer = CatalogSerializer(catalog)
		is_created(client, catalog._meta.model.__name__, serializer.data)

	def test_import_image(self, client, image):
		serializer = ImageSerializer(image)
		is_created(client, image._meta.model.__name__, serializer.data)
