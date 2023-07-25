import pytest
from attributes.serializers import AttributeNameSerializer, AttributeValueSerializer, AttributeSerializer
from attributes.models import AttributeName, AttributeValue, Attribute

pytestmark = pytest.mark.django_db


class TestSerializeAttributeModels:
	def test_serialize_attribute_name(self, attribute_name):
		serializer = AttributeNameSerializer(attribute_name)
		assert serializer.data['nazev'] == attribute_name.name
		assert serializer.data['kod'] == attribute_name.code
		assert serializer.data['zobrazit'] == attribute_name.show
		assert serializer.data['id']

	def test_deserialize_attribute_name(self, attribute_name):
		serializer = AttributeNameSerializer(attribute_name)
		assert serializer.data
		serializer = AttributeNameSerializer(data=serializer.data)
		assert serializer.is_valid()

	def test_serialize_attribute_value(self, attribute_value):
		serializer = AttributeValueSerializer(attribute_value)
		assert serializer.data['hodnota'] == attribute_value.value
		assert serializer.data['id']

	def test_deserialize_attribute_value(self, attribute_value):
		serializer = AttributeValueSerializer(attribute_value)
		assert serializer.data
		serializer = AttributeValueSerializer(data=serializer.data)
		assert serializer.is_valid()

	def test_serialize_attribute(self, attribute_value, attribute_name):
		attribute = Attribute(id=1337)
		attribute.attribute_name = attribute_name
		attribute.attribute_value = attribute_value
		serializer = AttributeSerializer(attribute)
		assert serializer.data['id'] == 1337
		assert serializer.data['nazev_atributu_id'] == attribute_name.id
		assert serializer.data['hodnota_atributu_id'] == attribute_value.id

	def test_deserialize_attribute(self, attribute_value, attribute_name):
		attribute = Attribute(id=228)
		attribute.attribute_name = attribute_name
		attribute.attribute_value = attribute_value
		serializer = AttributeSerializer(attribute)
		assert serializer.data
		serializer = AttributeSerializer(data=serializer.data)
		assert serializer.is_valid()

	def test_serialize_attribute_with_factory(self, attribute):
		attr_name = attribute.attribute_name
		attr_value = attribute.attribute_value
		serializer = AttributeSerializer(attribute)
		assert serializer.data['id']
		assert serializer.data['nazev_atributu_id'] == attr_name.id
		assert serializer.data['hodnota_atributu_id'] == attr_value.id

	def test_deserialize_attribute_with_factory(self, attribute):
		serializer = AttributeSerializer(attribute)
		assert serializer.data
		serializer = AttributeSerializer(data=serializer.data)
		assert serializer.is_valid()
