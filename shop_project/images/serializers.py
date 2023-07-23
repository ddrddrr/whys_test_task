from rest_framework import serializers
from api.serializer_mixins import SerializerUrlMixin
from .models import Image


class ImageSerializer(SerializerUrlMixin, serializers.ModelSerializer):
	obrazek = serializers.URLField(source='source_url')
	nazev = serializers.CharField(source='name', required=False)

	class Meta:
		model = Image
		fields = [
			'id',
			'url',
			'obrazek',
			'nazev',
		]
