from django.core.management.base import BaseCommand
from ._private import create, ModelCreateMixin, faker

payload_image = {
	"Image": {
		"nazev": faker.word(),
		"obrazek": faker.url()
	}
}


def create_image(payload=payload_image):
	return create(payload)


mf_map = {
	'image': create_image
}


class Command(BaseCommand, ModelCreateMixin):
	def add_arguments(self, parser):
		parser.add_argument('create_images', nargs='*', type=str)

	def handle(self, *args, **options):
		if not options['create_images']:
			for model_name in mf_map.keys():
				self.create_model(model_name, mf_map)
		for model_name in options['create_images']:
			self.create_model(model_name, mf_map)
