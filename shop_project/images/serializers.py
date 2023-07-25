from rest_framework import serializers
from api.serializers import UrlIdSerializer
from .models import Image


class ImageSerializer(UrlIdSerializer):
	obrazek = serializers.URLField(source='source_url')
	nazev = serializers.CharField(
			source='name',
			required=False,
			allow_blank=True
	)

	class Meta:
		model = Image
		fields = [
			'id',
			'url',
			'obrazek',
			'nazev',
		]
