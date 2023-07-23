from rest_framework import serializers
from attributes.serializers import AttributeSerializer, DetailedAttributeSerializer
from attributes.models import Attribute
from images.models import Image
from images.serializers import ImageSerializer
from .models import Product, ProductImage, ProductAttributes, Catalog
from api.serializer_mixins import SerializerUrlMixin


# Explicitly providing fields is more readable than __all__
class ProductSerializer(SerializerUrlMixin, serializers.ModelSerializer):
	nazev = serializers.CharField(source='name', required=False)
	cena = serializers.DecimalField(source='price', max_digits=12, decimal_places=2)
	mena = serializers.CharField(source='currency')

	class Meta:
		model = Product
		fields = [
			'id',
			'url',
			'nazev',
			'description',
			'cena',
			'mena',
			'published_on',
			'is_published',
		]


class ProductAttributesSerializer(SerializerUrlMixin, serializers.ModelSerializer):
	product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
	attribute = serializers.PrimaryKeyRelatedField(queryset=Attribute.objects.all())

	class Meta:
		model = ProductAttributes
		fields = [
			'id',
			'url',
			'attribute',
			'product',
		]


class ProductImageSerializer(SerializerUrlMixin, serializers.ModelSerializer):
	product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
	obrazek_id = serializers.PrimaryKeyRelatedField(queryset=Image.objects.all(), source='image')
	nazev = serializers.CharField(source='name', required=False)

	class Meta:
		model = ProductImage
		fields = [
			'id',
			'url',
			'product',
			'obrazek_id',
			'nazev',
		]


class CatalogSerializer(SerializerUrlMixin, serializers.ModelSerializer):
	obrazek_id = serializers.PrimaryKeyRelatedField(
			queryset=Image.objects.all(),
			required=False,
			source='image'
	)
	products_ids = serializers.PrimaryKeyRelatedField(
			many=True,
			required=False,
			queryset=Product.objects.all(),
			source='products'
	)
	attributes_ids = serializers.PrimaryKeyRelatedField(
			many=True,
			required=False,
			queryset=Attribute.objects.all(),
			source='attributes'
	)
	nazev = serializers.CharField(source='name', required=False)

	class Meta:
		model = Catalog
		fields = [
			'id',
			'url',
			'nazev',
			'obrazek_id',
			'products_ids',
			'attributes_ids',
		]

# class DetailedProductSerializer(ProductSerializer):
# 	attributes = serializers.PrimaryKeyRelatedField(many=True, queryset=Attribute.objects.all())
# 	image = serializers.PrimaryKeyRelatedField(queryset=Image.objects.all())
#
# 	class Meta:
# 		model = Product
# 		fields = ProductSerializer.Meta.fields + ['attributes', 'image']


# class DetailedCatalogSerializer(CatalogSerializer):
# 	products = DetailedProductSerializer(
# 			required=False,
# 			many=True,
# 			source='products_ids',
# 			read_only=True
# 	)
#
# 	attributes = DetailedAttributeSerializer(
# 			required=False,
# 			many=True,
# 			source='attributes_ids',
# 			read_only=True
# 	)
#
# 	class Meta:
# 		model = Catalog
# 		fields = CatalogSerializer.Meta.fields + ['products']
