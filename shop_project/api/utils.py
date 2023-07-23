from django.apps import apps
from typing import Dict
import importlib


# assuming model names are unique
class ModelToSerializersFieldsMapping:
	"""
	    Utility class with model_name - model - serializer and model_name - fields mappings.
        model_serializer_mapping (dict): A mapping between model names (lowercase) and corresponding model and serializer classes.
        model_field_names_mapping (dict): A mapping between model names (lowercase) and custom field names for serialization.
    """

	def __init__(self):
		self.model_serializer_mapping = dict()
		self.model_field_names_mapping = dict()
		for config in apps.get_app_configs():
			root_module_name = config.name
			for model in config.get_models():
				model_name = model.__name__
				serializer_classes = self.get_serializer_classes(model_name, root_module_name)
				field_mapping = self.get_field_mapping(root_module_name)
				if serializer_classes is not None:
					self.model_serializer_mapping[model_name.lower()] = (model, serializer_classes)
				if field_mapping is not None:
					self.model_field_names_mapping[model_name.lower()] = field_mapping

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

	@staticmethod
	def get_field_mapping(root_module_name):
		try:
			field_mapping_module = importlib.import_module(f"{root_module_name}.field_mapping")
			return getattr(field_mapping_module, f"{root_module_name.upper()}_FIELDS_MAPPING", dict())
		except ImportError:
			return None

	def get_model_and_serializers(self, model_name):
		return self.model_serializer_mapping.get(model_name.lower(), (None, None))

	def get_field_map(self, model_name):
		return self.model_field_names_mapping.get(model_name.lower(), None)


MODEL_TO_SERIALIZERS_MAP = ModelToSerializersFieldsMapping()


def change_attribute_names(attributes: Dict[str, str], field_mapping: Dict[str, str]):
	new_attrs = dict()
	for attribute in attributes:
		new_name = field_mapping.get(attribute.lower(), '')
		if new_name:
			new_attrs[new_name] = attributes[attribute]
		else:
			new_attrs[attribute] = attributes[attribute]
	return new_attrs
