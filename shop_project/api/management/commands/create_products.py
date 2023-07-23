from django.core.management.base import BaseCommand, CommandError
from random import randint
from ._private import get_model_name, create, ModelCreateMixin, faker
from .create_attributes import create_attribute
from .create_images import create_image

payload_product = {
	"Product": {
		"nazev": faker.word(),
		"description": faker.text(max_nb_chars=100),
		"cena": faker.pyint(min_value=1, max_value=10000),
		"mena": "CZK",
		"published_on": faker.date(),
		"is_published": faker.pybool()
	}
}

payload_product_attrs = {
	"ProductAttributes": {
	}
}

payload_product_image = {
	"ProductImage": {
		"nazev": faker.word()
	}
}

payload_catalog = {
	"Catalog": {
		"nazev": faker.word()
	}
}


def create_product(payload=payload_product):
	return create(payload)


def create_product_attributes(payload=payload_product_attrs):
	model_name = get_model_name(payload)
	payload[model_name]['product'] = create_product()
	payload[model_name]['attribute'] = create_attribute()
	return create(payload)


def create_product_image(payload=payload_product_image):
	model_name = get_model_name(payload)
	payload[model_name]['product'] = create_product()
	payload[model_name]['obrazek_id'] = create_image()
	return create(payload)


def create_catalog(payload=payload_catalog):
	model_name = get_model_name(payload)
	payload[model_name]['products_ids'] = [create_product() for _ in range(randint(1, 3))]
	payload[model_name]['attributes_ids'] = [create_attribute() for _ in range(randint(1, 3))]
	payload[model_name]['obrazek_id'] = create_image()
	return create(payload)


mf_map = {
	'product': create_product,
	'productattributes': create_product_attributes,
	'productimage': create_product_image,
	'catalog': create_catalog,
}


class Command(BaseCommand, ModelCreateMixin):
	def add_arguments(self, parser):
		parser.add_argument('create_products', nargs='*', type=str)

	def handle(self, *args, **options):
		if not options['create_products']:
			for model_name in mf_map.keys():
				self.create_model(model_name, mf_map)

		for model_name in options['create_products']:
			self.create_model(model_name, mf_map)
