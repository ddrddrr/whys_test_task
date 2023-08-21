from rest_framework import serializers

from api.serializers import UrlIdSerializer

from attributes.serializers import DetailedAttributeSerializer
from attributes.models import Attribute

from images.models import Image
from images.serializers import ImageSerializer

from .models import Product, ProductImage, ProductAttributes, Catalog


# Explicitly providing fields is more readable than __all__
class ProductSerializer(UrlIdSerializer):
	nazev = serializers.CharField(
			source='name',
			required=False,
			allow_blank=True
	)
	cena = serializers.DecimalField(
			source='price',
			required=False,
			max_digits=10,
			decimal_places=2,
	)
	mena = serializers.CharField(
			source='currency',
			required=False,
			allow_blank=True
	)

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


class ProductAttributesSerializer(UrlIdSerializer):
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


class ProductImageSerializer(UrlIdSerializer):
	product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
	obrazek_id = serializers.PrimaryKeyRelatedField(queryset=Image.objects.all(), source='image')
	nazev = serializers.CharField(
			required=False,
			allow_blank=True,
			source='name'
	)

	class Meta:
		model = ProductImage
		fields = [
			'id',
			'url',
			'product',
			'obrazek_id',
			'nazev',
		]


class CatalogSerializer(UrlIdSerializer):
	obrazek_id = serializers.PrimaryKeyRelatedField(
			required=False,
			source='image',
			queryset=Image.objects.all(),
	)
	products_ids = serializers.PrimaryKeyRelatedField(
			many=True,
			required=False,
			source='products',
			queryset=Product.objects.all(),
	)
	attributes_ids = serializers.PrimaryKeyRelatedField(
			many=True,
			required=False,
			source='attributes',
			queryset=Attribute.objects.all(),
	)
	nazev = serializers.CharField(
			required=False,
			allow_blank=True,
			source='name',

	)

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
# 	attributes = DetailedAttributeSerializer(many=True, required=False, read_only=True)
# 	image = ImageSerializer(required=False)
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
