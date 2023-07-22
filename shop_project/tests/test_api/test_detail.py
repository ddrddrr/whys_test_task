import pytest
from api.model_serializers_map import MODEL_TO_SERIALIZERS_MAP as mts_map
from ..misc import TEST_DATA, get_detail_endpoint, get_model_name
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
	_, serializers = mts_map.mapping[model_name.lower()]
	serializer = serializers['regular']
	serializer = serializer(data=payload[model_name])
	if serializer.is_valid():
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
		model_name = attribute_name._meta.model.__name__
		serializer = AttributeNameSerializer(attribute_name)
		assert are_equal(client, model_name, serializer.data)

	def test_detail_attribute_value(self, client, attribute_value):
		model_name = attribute_value._meta.model.__name__
		serializer = AttributeValueSerializer(attribute_value)
		assert are_equal(client, model_name, serializer.data)

	def test_detail_attribute_serializers(self, client, attribute):
		model_name = attribute._meta.model.__name__
		serializer = AttributeSerializer(attribute)
		assert are_equal(client, model_name, serializer.data)

	def test_detail_product(self, client, product):
		model_name = product._meta.model.__name__
		serializer = ProductSerializer(product)
		assert are_equal(client, model_name, serializer.data)

	def test_detail_product_attributes(self, client, product_attributes):
		model_name = product_attributes._meta.model.__name__
		serializer = ProductAttributesSerializer(product_attributes)
		assert are_equal(client, model_name, serializer.data)

	def test_detail_product_image(self, client, product_image):
		model_name = product_image._meta.model.__name__
		serializer = ProductImageSerializer(product_image)
		assert are_equal(client, model_name, serializer.data)

	def test_detail_catalog(self, client, catalog):
		model_name = catalog._meta.model.__name__
		serializer = CatalogSerializer(catalog)
		assert are_equal(client, model_name, serializer.data)

	def test_detail_image(self, client, image):
		model_name = image._meta.model.__name__
		serializer = ImageSerializer(image)
		assert are_equal(client, model_name, serializer.data)
