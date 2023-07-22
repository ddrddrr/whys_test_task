import pytest


@pytest.fixture
def product_with_attributes_and_image(
		product_factory,
		product_attributes_factory,
		product_image_factory
):
	product = product_factory()
	attributes = product_attributes_factory.create_batch(3, product=product)
	image = product_image_factory(product=product)
	return product, attributes, image


@pytest.fixture
def catalog_with_products_and_attributes(
		catalog_factory,
		product_factory,
		attribute_factory
):
	catalog = catalog_factory()
	products = product_factory.create_batch(3)
	attributes = attribute_factory.create_batch(2)
	catalog.products_ids.add(*products)
	catalog.attributes_ids.add(*attributes)
	return catalog, products, attributes
