import importlib

from django.apps import apps

from rest_framework.response import Response
from rest_framework import status


# Assuming model names are unique
class ModelToSerializersMapping:
	"""
		Utility class with {model_name : (model , [serializer])} mappings.
		self.model_serializer_mapping contains mapping of lowercase model name, corresponding model class and
		serializer class
	"""

	def __init__(self):
		self.model_serializer_mapping = dict()
		for config in apps.get_app_configs():
			root_module_name = config.name
			for model in config.get_models():
				model_name = model.__name__
				serializer_classes = self.get_serializer_classes(model_name, root_module_name)
				if serializer_classes is not None:
					self.model_serializer_mapping[model_name.lower()] = (model, serializer_classes)

	@staticmethod
	def get_serializer_classes(model_name, root_module_name):
		try:
			serializers_module = importlib.import_module(f"{root_module_name}.serializers")
			return {
				"regular": getattr(serializers_module, f"{model_name}Serializer", ""),
				"detailed": getattr(serializers_module, f"Detailed{model_name}Serializer", "")
			}
		except ImportError:
			return None

	def get_model_and_serializers(self, model_name):
		return self.model_serializer_mapping.get(model_name.lower(), (None, None))


def custom_400(msg):
	return Response({'status': 'error', 'error': msg}, status=status.HTTP_400_BAD_REQUEST)


def get_model_name(data):
	name = list(data.keys())[0]
	return name
