from rest_framework import serializers
from .models import Attribute, AttributeName, AttributeValue
from api.serializer_mixins import SerializerUrlMixin


class AttributeNameSerializer(SerializerUrlMixin, serializers.ModelSerializer):
	class Meta:
		model = AttributeName
		fields = [
			'id',
			'nazev',
			'kod',
			'zobrazit',
		]


class AttributeValueSerializer(SerializerUrlMixin, serializers.ModelSerializer):
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
			source='nazev_atributu'
	)
	hodnota_atributu_id = serializers.PrimaryKeyRelatedField(
			queryset=AttributeValue.objects.all(),
			source='hodnota_atributu'
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
	attribute_name = AttributeNameSerializer(read_only=True, source='nazev_atributu')
	attribute_value = AttributeValueSerializer(read_only=True, source='hodnota_atributu')

	class Meta:
		model = Attribute
		fields = AttributeSerializer.Meta.fields + ['attribute_name', 'attribute_value']
