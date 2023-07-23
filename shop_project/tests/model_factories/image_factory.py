from factory import Faker
from factory.django import DjangoModelFactory
from images.models import Image


class ImageFactory(DjangoModelFactory):
	class Meta:
		model = Image

	source_url = Faker('url')
	name = Faker('word')
