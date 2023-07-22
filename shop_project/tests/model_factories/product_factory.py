from factory import Factory, Faker, SubFactory, post_generation
from factory.django import DjangoModelFactory
from products.models import Product, ProductAttributes, ProductImage, Catalog
from .image_factory import ImageFactory
from .attribute_factory import AttributeFactory
import random as r
from pytest_factoryboy import register


class CurrencyProvider(Factory):
	CURRENCIES = ['CZK', 'USD', 'EUR', 'GBP']

	@classmethod
	def random_currency(cls):
		return r.choice(cls.CURRENCIES)


class ProductFactory(DjangoModelFactory):
	class Meta:
		model = Product

	nazev = Faker('word')
	description = Faker('paragraph', nb_sentences=r.randint(1, 5))
	cena = Faker('pydecimal', left_digits=r.randint(1, 10), right_digits=r.randint(0, 2))
	mena = CurrencyProvider.random_currency()
	published_on = Faker('date_time_this_century')
	is_published = Faker('pybool')


class ProductImageFactory(DjangoModelFactory):
	class Meta:
		model = ProductImage

	product = SubFactory(ProductFactory)
	obrazek = SubFactory(ImageFactory)
	nazev = Faker('word')


class ProductAttributesFactory(DjangoModelFactory):
	class Meta:
		model = ProductAttributes

	attribute = SubFactory(AttributeFactory)
	product = SubFactory(ProductFactory)


class CatalogFactory(DjangoModelFactory):
	class Meta:
		model = Catalog

	nazev = Faker('word')
	obrazek = SubFactory(ImageFactory)

	@post_generation
	def products_ids(self, create, extracted, **kwargs):
		if not create or not extracted:
			return
		self.products_ids.add(*extracted)

	@post_generation
	def attributes_ids(self, create, extracted, **kwargs):
		if not create or not extracted:
			return
		self.attributes_ids.add(*extracted)
