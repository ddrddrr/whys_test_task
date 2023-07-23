from rest_framework import serializers
from .models import Attribute, AttributeName, AttributeValue
from api.serializer_mixins import SerializerUrlMixin


class AttributeNameSerializer(SerializerUrlMixin, serializers.ModelSerializer):
	nazev = serializers.CharField(source='name')
	kod = serializers.CharField(source='code', required=False)
	zobrazit = serializers.BooleanField(source='show', required=False)

	class Meta:
		model = AttributeName
		fields = [
			'id',
			'nazev',
			'kod',
			'zobrazit',
		]


class AttributeValueSerializer(SerializerUrlMixin, serializers.ModelSerializer):
	hodnota = serializers.CharField(source='value')

	class Meta:
		model = AttributeValue
		fields = [
			'id',
			'url',
			'hodnota',
		]


class AttributeSerializer(SerializerUrlMixin, serializers.ModelSerializer):
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
