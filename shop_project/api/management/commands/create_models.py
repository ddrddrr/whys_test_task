from django.core.management.base import BaseCommand
from ._private import ModelCreateMixin
from .creation_configs.products_create_config import mf_map as mf_map_products
from .creation_configs.attributes_create_config import mf_map as mf_map_attrs
from .creation_configs.images_create_config import mf_map as mf_map_images


MF_MAP = dict()
for mf_map in [mf_map_attrs, mf_map_images, mf_map_products]:
	for model, func in mf_map.items():
		MF_MAP[model] = func


class Command(BaseCommand, ModelCreateMixin):
	def add_arguments(self, parser):
		parser.add_argument('create_models', nargs='*', type=str)

	def handle(self, *args, **options):
		opt_args = options['create_models']
		if not opt_args:
			for model_name, creation_func in MF_MAP.items():
				self.create(creation_func, model_name)

		if 'create_products' in opt_args:
			self.create_all(mf_map_products)
		if 'create_attributes' in opt_args:
			self.create_all(mf_map_attrs)
		if 'create_images' in opt_args:
			self.create_all(mf_map_images)

		for arg in opt_args:
			if arg not in['create_products', 'create_attributes', 'create_images']:
				self.create_model(arg, MF_MAP)
