from .model_serializers_map import MODEL_TO_SERIALIZERS_MAP as mts_map
from rest_framework.exceptions import MethodNotAllowed, ValidationError
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404


# TODO custom errors (with 404 and others)
def get_model_name(request, kwargs):
	if request.method == 'GET':
		model_name = kwargs.get('model_name', '')
		if not model_name:
			raise Http404

	elif request.method == 'POST':
		data = request.data
		if not data:
			raise ValidationError
		try:
			model_name = list(data.keys())[0]
		except Exception as _:
			raise ValidationError

	else:
		raise MethodNotAllowed

	return model_name


class FindModelMixin:
	def get_object(self):
		model_name = get_model_name(self.request, self.kwargs)
		model, _ = mts_map.get_model_and_serializers(model_name)
		if model is not None and model.objects.exists():
			try:
				obj = model.objects.get(pk=self.kwargs['pk'])
			except ObjectDoesNotExist:
				raise Http404

			return obj
		raise Http404

	def get_queryset(self):
		model_name = get_model_name(self.request, self.kwargs)
		model, _ = mts_map.get_model_and_serializers(model_name)
		if model is not None and model.objects.exists():
			return model.objects.all()
		raise Http404


class FindSerializerClassMixin:
	def get_serializer_class(self):
		model_name = get_model_name(self.request, self.kwargs)
		_, serializer_classes = mts_map.get_model_and_serializers(model_name)
		if serializer_classes is not None:
			return serializer_classes["regular"]
		raise Http404


class GetDetailedSerializerMixin:
	def get_serializer_class(self):
		model_name = get_model_name(self.request, self.kwargs)
		_, serializer_classes = mts_map.get_model_and_serializers(model_name)
		if serializer_classes is not None:
			sz = serializer_classes.get('detailed', '')
			if sz == '':
				raise Http404
			return sz
		raise Http404


class GetRegularSerializerMixin:
	def get_serializer(self, *args, **kwargs):
		if self.request.method == 'POST':
			model_name = get_model_name(self.request, self.kwargs)
			attributes = self.request.data[model_name]
			stripped_data = {key: value for (key, value) in attributes.items()}
			kwargs['data'] = stripped_data
		return super().get_serializer(*args, **kwargs)


class DetaliedSerialierMixin(GetDetailedSerializerMixin, FindSerializerClassMixin):
	pass


class RegularSerialierMixin(GetRegularSerializerMixin, FindSerializerClassMixin):
	pass


class DetailedModelInfoMixin(DetaliedSerialierMixin, FindModelMixin):
	pass


class RegularModelInfoMixin(RegularSerialierMixin, FindModelMixin):
	pass

# def get_serializer_context(self):
# 	context = super().get_serializer_context()
# 	if self.request.method == 'POST':
# 		data = self.request.data
# 		model_name = list(data.keys())[0]
# 		context['custom_id'] = self.request.data[model_name]['id']
# 	return context
