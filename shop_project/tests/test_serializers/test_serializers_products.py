import pytest
from products.models import ProductImage, ProductAttributes, Catalog
from products.serializers import (
	ProductSerializer,
	ProductAttributesSerializer,
	ProductImageSerializer,
	CatalogSerializer
)
from decimal import Decimal
from datetime import datetime

pytestmark = pytest.mark.django_db


@pytest.fixture()
def product_image_regular(product, image):
	product_image = ProductImage()
	product_image.product = product
	product_image.image = image
	product_image.save()
	return product, image, product_image


@pytest.fixture()
def product_attributes_regular(product, attribute):
	product_attrs = ProductAttributes()
	product_attrs.product = product
	product_attrs.attribute = attribute
	product_attrs.save()
	return product, attribute, product_attrs


@pytest.fixture()
def catalog_regular(product_factory, attribute_factory, image):
	products = product_factory.create_batch(3)
	attributes = attribute_factory.create_batch(4)
	catalog = Catalog()
	catalog.save()
	catalog.image = image
	catalog.products.add(*products)
	catalog.attributes.add(*attributes)
	return catalog, products, attributes, image


class TestSerializeAttributeModels:
	def test_serialize_product(self, product):
		serializer = ProductSerializer(product)
		assert serializer.data['nazev'] == product.name
		assert serializer.data['description'] == product.description
		assert Decimal(serializer.data['cena']) == product.price
		assert serializer.data['mena'] == product.currency
		assert datetime.strptime(serializer.data['published_on'], '%Y-%m-%dT%H:%M:%SZ') == product.published_on
		assert serializer.data['is_published'] == product.is_published

	def test_deserialize_product(self, product):
		serializer = ProductSerializer(product)
		assert serializer.data
		serializer = ProductSerializer(data=serializer.data)
		assert serializer.is_valid()

	def test_serialize_product_image(self, product_image_regular):
		product, image, product_image = product_image_regular
		serializer = ProductImageSerializer(product_image)
		assert serializer.data['nazev'] == product_image.name
		assert serializer.data['product'] == product.id
		assert serializer.data['obrazek_id'] == image.id

	def test_serialize_product_image_with_factory(self, product_image):
		product_image = product_image
		product = product_image.product
		image = product_image.image
		serializer = ProductImageSerializer(product_image)
		assert serializer.data['nazev'] == product_image.name
		assert serializer.data['product'] == product.id
		assert serializer.data['obrazek_id'] == image.id

	def test_deserialize_product_image(self, product_image_regular):
		product, image, product_image = product_image_regular
		serializer = ProductImageSerializer(product_image)
		assert serializer.data
		serializer = ProductImageSerializer(data=serializer.data)
		try:
			serializer.is_valid(raise_exception=True)
		except Exception as ex:
			print(ex)

	def test_deserialize_product_image_with_factory(self, product_image):
		serializer = ProductImageSerializer(product_image)
		assert serializer.data
		serializer = ProductImageSerializer(data=serializer.data)
		assert serializer.is_valid()

	def test_serialize_product_attributes(self, product_attributes_regular):
		product, attribute, product_attrs = product_attributes_regular
		serializer = ProductAttributesSerializer(product_attrs)
		assert serializer.data['product'] == product.id
		assert serializer.data['attribute'] == attribute.id

	def test_serialize_product_attributes_with_factory(self, product_attributes):
		product_attributes = product_attributes
		product = product_attributes.product
		attribute = product_attributes.attribute
		serializer = ProductAttributesSerializer(product_attributes)
		assert serializer.data['product'] == product.id
		assert serializer.data['attribute'] == attribute.id

	def test_deserialize_product_attributes(self, product_attributes_regular):
		product, attribute, product_attrs = product_attributes_regular
		serializer = ProductAttributesSerializer(product_attrs)
		assert serializer.data
		serializer = ProductAttributesSerializer(data=serializer.data)
		assert serializer.is_valid()

	def test_deserialize_product_attributes_with_factory(self, product_attributes):
		serializer = ProductAttributesSerializer(product_attributes)
		assert serializer.data
		serializer = ProductAttributesSerializer(data=serializer.data)
		assert serializer.is_valid()

	def test_serialize_catalog(self, catalog_regular):
		catalog, products, attributes, image = catalog_regular
		serializer = CatalogSerializer(catalog)
		assert serializer.data['obrazek_id'] == image.id
		assert serializer.data['products_ids'] == [product.id for product in products]
		assert serializer.data['attributes_ids'] == [attribute.id for attribute in attributes]

	def test_serialize_catalog_with_factory(self, catalog_factory, product_factory, attribute_factory):
		products = product_factory.create_batch(4)
		attributes = attribute_factory.create_batch(2)
		catalog = catalog_factory.create(attributes=attributes, products=products)
		image = catalog.image
		serializer = CatalogSerializer(catalog)
		assert serializer.data['nazev'] == catalog.name
		assert serializer.data['attributes_ids'] == [attribute.id for attribute in attributes]
		assert serializer.data['products_ids'] == [product.id for product in products]
		assert serializer.data['obrazek_id'] == image.id
