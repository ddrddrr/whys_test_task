import random as r

from factory import Factory, Faker, SubFactory, post_generation

from products.models import Product, ProductAttributes, ProductImage, Catalog

from .image_factory import ImageFactory
from .attribute_factory import AttributeFactory
from .base_factory import UserIdFactory


class CurrencyProvider(Factory):
	CURRENCIES = ['CZK', 'USD', 'EUR', 'GBP']

	@classmethod
	def random_currency(cls):
		return r.choice(cls.CURRENCIES)


class ProductFactory(UserIdFactory):
	class Meta:
		model = Product

	name = Faker('word')
	description = Faker('paragraph', nb_sentences=r.randint(1, 5))
	price = Faker('pydecimal', left_digits=r.randint(1, 10), right_digits=r.randint(0, 2))
	currency = CurrencyProvider.random_currency()
	published_on = Faker('date_time_this_century')
	is_published = Faker('pybool')


class ProductImageFactory(UserIdFactory):
	class Meta:
		model = ProductImage

	product = SubFactory(ProductFactory)
	image = SubFactory(ImageFactory)
	name = Faker('word')


class ProductAttributesFactory(UserIdFactory):
	class Meta:
		model = ProductAttributes

	attribute = SubFactory(AttributeFactory)
	product = SubFactory(ProductFactory)


class CatalogFactory(UserIdFactory):
	class Meta:
		model = Catalog

	name = Faker('word')
	image = SubFactory(ImageFactory)

	@post_generation
	def products(self, create, extracted, **kwargs):
		if not create or not extracted:
			return
		self.products.add(*extracted)

	@post_generation
	def attributes(self, create, extracted, **kwargs):
		if not create or not extracted:
			return
		self.attributes.add(*extracted)
