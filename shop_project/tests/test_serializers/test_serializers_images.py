import pytest
from images.serializers import ImageSerializer

pytestmark = pytest.mark.django_db


class TestSerializeAttributeModels:
	def test_serialize_image(self, image):
		serializer = ImageSerializer(image)
		assert serializer.data['obrazek'] == image.source_url
		assert serializer.data['nazev'] == image.name

	def test_deserialize_image(self, image):
		serializer = ImageSerializer(image)
		assert serializer.data
		serializer = ImageSerializer(data=serializer.data)
		assert serializer.is_valid()
