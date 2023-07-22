import pytest
from images.serializers import ImageSerializer

pytestmark = pytest.mark.django_db


class TestSerializeAttributeModels:
	def test_serialize_image(self, image_factory):
		image = image_factory()
		serializer = ImageSerializer(image)
		assert serializer.data['obrazek'] == image.obrazek
		assert serializer.data['nazev'] == image.nazev

	def test_deserialize_image(self, image_factory):
		image = image_factory()
		serializer = ImageSerializer(image)
		assert serializer.data
		serializer = ImageSerializer(data=serializer.data)
		assert serializer.is_valid()
