from rest_framework import serializers
from .models import Attribute, AttributeName, AttributeValue
from api.serializers import UrlIdSerializer


class AttributeNameSerializer(UrlIdSerializer):
	nazev = serializers.CharField(
			source='name',
			required=False,
			allow_blank=True
	)
	kod = serializers.CharField(
			source='code',
			required=False,
			allow_blank=True
	)
	zobrazit = serializers.BooleanField(source='show', required=False)

	class Meta:
		model = AttributeName
		fields = [
			'id',
			'nazev',
			'kod',
			'zobrazit',
		]


class AttributeValueSerializer(UrlIdSerializer):
	hodnota = serializers.CharField(source='value')

	class Meta:
		model = AttributeValue
		fields = [
			'id',
			'url',
			'hodnota',
		]


class AttributeSerializer(UrlIdSerializer):
	nazev_atributu_id = serializers.PrimaryKeyRelatedField(
			queryset=AttributeName.objects.all(),
			source='attribute_name'
	)
	hodnota_atributu_id = serializers.PrimaryKeyRelatedField(
			queryset=AttributeValue.objects.all(),
			source='attribute_value'
	)

	class Meta:
		model = Attribute
		fields = [
			'id',
			'url',
			'nazev_atributu_id',
			'hodnota_atributu_id',
		]


class DetailedAttributeSerializer(AttributeSerializer):
	attribute_name = AttributeNameSerializer(read_only=True)
	attribute_value = AttributeValueSerializer(read_only=True)

	class Meta:
		model = Attribute
		fields = AttributeSerializer.Meta.fields + ['attribute_name', 'attribute_value']
