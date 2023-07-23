from django.core.management.base import BaseCommand
from ._private import get_model_name, create, ModelCreateMixin, faker

payload_attr_name = {
	"AttributeName": {
		"nazev": faker.word()
	}
}

payload_attr_val = {
	"AttributeValue": {
		"hodnota": faker.word()
	}
}

payload_attr = {
	"Attribute": {
	}
}


def create_attribute_name(payload=payload_attr_name):
	return create(payload)


def create_attribute_value(payload=payload_attr_val):
	return create(payload)


def create_attribute(payload=payload_attr):
	model_name = get_model_name(payload)
	payload[model_name]['nazev_atributu_id'] = create_attribute_name(payload_attr_name)
	payload[model_name]['hodnota_atributu_id'] = create_attribute_value(payload_attr_val)
	return create(payload)


mf_map = {
	'attributename': create_attribute_name,
	'attributevalue': create_attribute_value,
	'attribute': create_attribute
}


class Command(BaseCommand, ModelCreateMixin):
	def add_arguments(self, parser):
		parser.add_argument('create_attributes', nargs='*', type=str)

	def handle(self, *args, **options):
		if not options['create_attributes']:
			for model_name in mf_map.keys():
				self.create_model(model_name, mf_map)

		for model_name in options['create_attributes']:
			self.create_model(model_name, mf_map)
