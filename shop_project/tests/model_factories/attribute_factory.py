from factory import Faker, SubFactory
from factory.django import DjangoModelFactory
from attributes.models import AttributeName, AttributeValue, Attribute
from pytest_factoryboy import register


class AttributeNameFactory(DjangoModelFactory):
	class Meta:
		model = AttributeName

	nazev = Faker('word')
	kod = Faker('word')
	zobrazit = Faker('pybool')


class AttributeValueFactory(DjangoModelFactory):
	class Meta:
		model = AttributeValue

	hodnota = Faker('word')


class AttributeFactory(DjangoModelFactory):
	class Meta:
		model = Attribute

	nazev_atributu = SubFactory(AttributeNameFactory)
	hodnota_atributu = SubFactory(AttributeValueFactory)
