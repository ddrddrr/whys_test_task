from rest_framework import serializers
from attributes.serializers import AttributeSerializer, DetailedAttributeSerializer
from attributes.models import Attribute
from images.models import Image
from images.serializers import ImageSerializer
from .models import Product, ProductImage, ProductAttributes, Catalog
from api.serializers import UrlIdSerializer


# Explicitly providing fields is more readable than __all__
class ProductSerializer(UrlIdSerializer):
	nazev = serializers.CharField(
			source='name',
			required=False,
			allow_blank=True
	)
	cena = serializers.DecimalField(
			source='price',
			max_digits=12,
			decimal_places=2,
			required=False
	)
	mena = serializers.CharField(
			source='currency',
			required=False,
			allow_blank=True)

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
	nazev = serializers.CharField(
			source='name',
			required=False,
			allow_blank=True)

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

	def create(self, validated_data):
		catalog = Catalog(id=validated_data['id'])
		catalog.save()
		name = validated_data.get('nazev', '')
		image = validated_data.get('obrazek_id', '')
		products = validated_data.get('products_ids', '')
		attributes = validated_data.get('attributes_ids', '')
		if products:
			catalog.products.set(products)
		if attributes:
			catalog.attributes.set(attributes)
		if name:
			catalog.name = name
		if image:
			catalog.image = image

		catalog.save()
		return catalog
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
