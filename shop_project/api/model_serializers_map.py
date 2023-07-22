from django.apps import apps
import importlib


# assuming model names are unique
class ModelToSerializersMapping:
	def __init__(self):
		self.mapping = dict()
		for config in apps.get_app_configs():
			root_module_name = config.name
			for model in config.get_models():
				model_name = model.__name__
				serializer_classes = self.get_serializer_classes(model_name, root_module_name)
				if serializer_classes is not None:
					self.mapping[model_name.lower()] = (model, serializer_classes)

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
		model_name = model_name.lower()
		return self.mapping.get(model_name, (None, None))


MODEL_TO_SERIALIZERS_MAP = ModelToSerializersMapping()
