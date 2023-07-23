from factory import Faker, SubFactory
from factory.django import DjangoModelFactory
from attributes.models import AttributeName, AttributeValue, Attribute


class AttributeNameFactory(DjangoModelFactory):
	class Meta:
		model = AttributeName

	name = Faker('word')
	code = Faker('word')
	show = Faker('pybool')


class AttributeValueFactory(DjangoModelFactory):
	class Meta:
		model = AttributeValue

	value = Faker('word')


class AttributeFactory(DjangoModelFactory):
	class Meta:
		model = Attribute

	attribute_name = SubFactory(AttributeNameFactory)
	attribute_value = SubFactory(AttributeValueFactory)
