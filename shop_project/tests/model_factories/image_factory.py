from factory import Faker
from factory.django import DjangoModelFactory
from images.models import Image
from .base_factory import UserIdFactory


class ImageFactory(UserIdFactory):
	class Meta:
		model = Image

	source_url = Faker('url')
	name = Faker('word')
