from factory import Faker
from factory.django import DjangoModelFactory
from images.models import Image
from pytest_factoryboy import register


class ImageFactory(DjangoModelFactory):
	class Meta:
		model = Image

	obrazek = Faker('url')
	nazev = Faker('word')
