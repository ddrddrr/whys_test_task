from factory import create_batch
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
def product_image_regular(product_factory, image_factory):
	product = product_factory()
	image = image_factory()
	product_image = ProductImage()
	product_image.product = product
	product_image.obrazek = image
	product_image.save()
	return product, image, product_image


@pytest.fixture()
def product_attributes_regular(product_factory, attribute_factory):
	product = product_factory()
	attribute = attribute_factory()
	product_attrs = ProductAttributes()
	product_attrs.product = product
	product_attrs.attribute = attribute
	product_attrs.save()
	return product, attribute, product_attrs


@pytest.fixture()
def catalog_regular(product_factory, attribute_factory, image_factory):
	image = image_factory()
	products = product_factory.create_batch(3)
	attributes = attribute_factory.create_batch(4)
	catalog = Catalog()
	catalog.save()
	catalog.obrazek = image
	catalog.products_ids.add(*products)
	catalog.attributes_ids.add(*attributes)
	return catalog, products, attributes, image


class TestSerializeAttributeModels:
	def test_serialize_product(self, product_factory):
		product = product_factory()
		serializer = ProductSerializer(product)
		assert serializer.data['nazev'] == product.nazev
		assert serializer.data['description'] == product.description
		assert Decimal(serializer.data['cena']) == product.cena
		assert serializer.data['mena'] == product.mena
		assert datetime.strptime(serializer.data['published_on'], '%Y-%m-%dT%H:%M:%SZ') == product.published_on
		assert serializer.data['is_published'] == product.is_published

	def test_deserialize_product(self, product_factory):
		product = product_factory()
		serializer = ProductSerializer(product)
		assert serializer.data
		serializer = ProductSerializer(data=serializer.data)
		assert serializer.is_valid()

	def test_serialize_product_image(self, product_image_regular):
		product, image, product_image = product_image_regular
		serializer = ProductImageSerializer(product_image)
		assert serializer.data['nazev'] == product_image.nazev
		assert serializer.data['product'] == product.id
		assert serializer.data['obrazek_id'] == image.id

	def test_serialize_product_image_with_factory(self, product_image_factory):
		product_image = product_image_factory()
		product = product_image.product
		image = product_image.obrazek
		serializer = ProductImageSerializer(product_image)
		assert serializer.data['nazev'] == product_image.nazev
		assert serializer.data['product'] == product.id
		assert serializer.data['obrazek_id'] == image.id

	def test_deserialize_product_image(self, product_image_regular):
		product, image, product_image = product_image_regular
		serializer = ProductImageSerializer(product_image)
		assert serializer.data
		serializer = ProductImageSerializer(data=serializer.data)
		assert serializer.is_valid()

	def test_deserialize_product_image_with_factory(self, product_image_factory):
		product_image = product_image_factory()
		serializer = ProductImageSerializer(product_image)
		assert serializer.data
		serializer = ProductImageSerializer(data=serializer.data)
		assert serializer.is_valid()

	def test_serialize_product_attributes(self, product_attributes_regular):
		product, attribute, product_attrs = product_attributes_regular
		serializer = ProductAttributesSerializer(product_attrs)
		assert serializer.data['product'] == product.id
		assert serializer.data['attribute'] == attribute.id

	def test_serialize_product_attributes_with_factory(self, product_attributes_factory):
		product_attributes = product_attributes_factory()
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

	def test_deserialize_product_attributes_with_factory(self, product_attributes_factory):
		product_attributes = product_attributes_factory()
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
		catalog = catalog_factory.create(attributes_ids=attributes, products_ids=products)
		image = catalog.obrazek
		serializer = CatalogSerializer(catalog)
		assert serializer.data['nazev'] == catalog.nazev
		assert serializer.data['attributes_ids'] == [attribute.id for attribute in attributes]
		assert serializer.data['products_ids'] == [product.id for product in products]
		assert serializer.data['obrazek_id'] == image.id
