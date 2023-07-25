from factory import Faker, SubFactory
from attributes.models import AttributeName, AttributeValue, Attribute
from .base_factory import UserIdFactory


class AttributeNameFactory(UserIdFactory):
	class Meta:
		model = AttributeName

	name = Faker('word')
	code = Faker('word')
	show = Faker('pybool')


class AttributeValueFactory(UserIdFactory):
	class Meta:
		model = AttributeValue

	value = Faker('word')


class AttributeFactory(UserIdFactory):
	class Meta:
		model = Attribute

	attribute_name = SubFactory(AttributeNameFactory)
	attribute_value = SubFactory(AttributeValueFactory)
