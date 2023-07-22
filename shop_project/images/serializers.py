from rest_framework import serializers
from api.serializer_mixins import SerializerUrlMixin
from .models import Image

class ImageSerializer(SerializerUrlMixin, serializers.ModelSerializer):
	class Meta:
		model = Image
		fields = [
			'id',
			#'url',
			'obrazek',
			'nazev',
		]
