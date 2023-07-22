import pytest
from attributes.serializers import AttributeNameSerializer, AttributeValueSerializer, AttributeSerializer
from attributes.models import AttributeName, AttributeValue, Attribute

pytestmark = pytest.mark.django_db


class TestSerializeAttributeModels:
	def test_serialize_attribute_name(self, attribute_name_factory):
		attr_name = attribute_name_factory()
		serializer = AttributeNameSerializer(attr_name)
		assert serializer.data['nazev'] == attr_name.nazev
		assert serializer.data['kod'] == attr_name.kod
		assert serializer.data['zobrazit'] == attr_name.zobrazit

	def test_deserialize_attribute_name(self, attribute_name_factory):
		attr_name = attribute_name_factory()
		serializer = AttributeNameSerializer(attr_name)
		assert serializer.data
		serializer = AttributeNameSerializer(data=serializer.data)
		assert serializer.is_valid()

	def test_serialize_attribute_value(self, attribute_value_factory):
		attr_name = attribute_value_factory()
		serializer = AttributeValueSerializer(attr_name)
		assert serializer.data['hodnota'] == attr_name.hodnota

	def test_deserialize_attribute_value(self, attribute_value_factory):
		attr_value = attribute_value_factory()
		serializer = AttributeValueSerializer(attr_value)
		assert serializer.data
		serializer = AttributeValueSerializer(data=serializer.data)
		assert serializer.is_valid()

	def test_serialize_attribute(self, attribute_value_factory, attribute_name_factory):
		attr_name = attribute_name_factory()
		attr_value = attribute_value_factory()
		attribute = Attribute()
		attribute.nazev_atributu = attr_name
		attribute.hodnota_atributu = attr_value
		serializer = AttributeSerializer(attribute)
		assert serializer.data['nazev_atributu_id'] == attr_name.id
		assert serializer.data['hodnota_atributu_id'] == attr_value.id

	def test_deserialize_attribute(self, attribute_value_factory, attribute_name_factory):
		attr_name = attribute_name_factory()
		attr_value = attribute_value_factory()
		attribute = Attribute()
		attribute.nazev_atributu = attr_name
		attribute.hodnota_atributu = attr_value
		serializer = AttributeSerializer(attribute)
		assert serializer.data
		serializer = AttributeSerializer(data=serializer.data)
		assert serializer.is_valid()

	def test_serialize_attribute_with_factory(self, attribute_factory):
		attribute = attribute_factory()
		attr_name = attribute.nazev_atributu
		attr_value = attribute.hodnota_atributu
		serializer = AttributeSerializer(attribute)
		assert serializer.data['nazev_atributu_id'] == attr_name.id
		assert serializer.data['hodnota_atributu_id'] == attr_value.id

	def test_deserialize_attribute_with_factory(self, attribute_factory):
		attribute = attribute_factory()
		serializer = AttributeSerializer(attribute)
		assert serializer.data
		serializer = AttributeSerializer(data=serializer.data)
		assert serializer.is_valid()
