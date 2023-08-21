import pytest
import json

from api.utils import ModelToSerializersMapping

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

from ..misc import TEST_DATA, get_detail_endpoint, get_model_name

MTS_MAP = ModelToSerializersMapping()
pytestmark = pytest.mark.django_db


def test_detail(client, model_instance, serializer_class):
	model_name = model_instance._meta.model.__name__
	serializer = serializer_class(model_instance)
	assert are_equal(client, model_name, serializer.data)


def are_equal(client, model_name, data):
	payload = json.dumps({model_name: data})
	response = client.get(get_detail_endpoint(payload))
	content = json.loads(response.content)
	assert response.status_code == 200
	for field in data.keys():
		if field != 'url' and data[field] != content[field]:
			return False
	return True


def create_model(payload):
	model_name = get_model_name(payload)
	_, serializers = MTS_MAP.model_serializer_mapping[model_name.lower()]
	serializer = serializers['regular']
	serializer = serializer(data=payload[model_name])
	try:
		serializer.is_valid(raise_exception=True)
	except Exception as ex:
		print(ex)
	else:
		serializer.save()
		return serializer.data


class TestModelDetail:
	def test_detail_task_data(self, client):
		with open(TEST_DATA, mode='r', encoding='utf-8') as td:
			test_data = json.load(td)
			for payload in test_data:
				create_model(payload)
				response = client.get(get_detail_endpoint(payload))
				assert response.status_code == 200

	def test_detail_attribute_name(self, client, attribute_name):
		test_detail(client, attribute_name, AttributeNameSerializer)

	def test_detail_attribute_value(self, client, attribute_value):
		test_detail(client, attribute_value, AttributeValueSerializer)

	def test_detail_attribute_serializers(self, client, attribute):
		test_detail(client, attribute, AttributeSerializer)

	def test_detail_image(self, client, image):
		test_detail(client, image, ImageSerializer)

	def test_detail_product(self, client, product):
		test_detail(client, product, ProductSerializer)

	def test_detail_product_attributes(self, client, product_attributes):
		test_detail(client, product_attributes, ProductAttributesSerializer)

	def test_detail_product_image(self, client, product_image):
		test_detail(client, product_image, ProductImageSerializer)

	def test_detail_catalog(self, client, catalog):
		test_detail(client, catalog, CatalogSerializer)
