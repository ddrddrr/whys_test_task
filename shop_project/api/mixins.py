from rest_framework.exceptions import MethodNotAllowed, ParseError, ValidationError

from django.http import Http404
from django.shortcuts import get_object_or_404

from .utils import ModelToSerializersMapping

MTS_MAP = ModelToSerializersMapping()


def get_serializer_class(model_name):
	_, serializer_classes = MTS_MAP.get_model_and_serializers(model_name)
	if serializer_classes is not None:
		# mapping contains only instances of regular and/or detailed serializers
		return serializer_classes['regular']
	return None


def get_model_name(request, kwargs=None) -> str:
	if request.method == 'GET':
		model_name = kwargs.get('model_name', '')
		if not model_name:
			raise Http404

	elif request.method == 'POST':
		data = request.data
		if not data:
			raise ParseError
		try:
			model_name = list(data.keys())[0]
		except Exception as _:
			raise ValidationError

	else:
		raise MethodNotAllowed

	return model_name


class FindModelMixin:
	"""
	Overrides basic get_object and get_queryset methods.
	get_queryset returns model queryset based on a model name.
	get_object, if provided the pk, returns model instance with given name and pk.
	"""

	def get_object(self):
		model_name = get_model_name(self.request, self.kwargs)
		model, _ = MTS_MAP.get_model_and_serializers(model_name)
		if model is not None and model.objects.exists():
			obj = get_object_or_404(model, pk=self.kwargs['pk'])
			return obj
		raise Http404

	def get_queryset(self):
		model_name = get_model_name(self.request, self.kwargs)
		model, _ = MTS_MAP.get_model_and_serializers(model_name)
		if model is not None and model.objects.exists():
			return model.objects.all()
		raise Http404


class GetRegularSerializerClassMixin:
	"""
	Overrides basic get_serializer_class method.
	Returns model's regular serializer based on model's name if it exists.
	"""

	def get_serializer_class(self):
		model_name = get_model_name(self.request, self.kwargs)
		_, serializer_classes = MTS_MAP.get_model_and_serializers(model_name)
		if serializer_classes is not None:
			# mapping contains only instances of regular and/or detailed serializers
			return serializer_classes['regular']
		raise Http404


class GetDetailedSerializerClassMixin:
	"""
		Overrides basic get_serializer_class method.
		Returns model's regular serializer based on model's name if it exists.
	"""

	def get_serializer_class(self):
		model_name = get_model_name(self.request, self.kwargs)
		_, serializer_classes = MTS_MAP.get_model_and_serializers(model_name)
		if serializer_classes is not None:
			sz = serializer_classes.get('detailed', '')
			if sz == '':
				raise Http404
			return sz
		raise Http404


class GetRegularSerializerMixin:
	"""
		Overrides basic get_serializer method.
		Returns model's regular serializer instance based on model's name if it exists.
	"""

	def get_serializer(self, *args, **kwargs):
		if self.request.method == 'POST':
			model_name = get_model_name(self.request)
			kwargs['data'] = self.request.data[model_name]
		return super().get_serializer(*args, **kwargs)


class RegularSerialierMixin(GetRegularSerializerMixin, GetRegularSerializerClassMixin):
	pass


class DetaliedSerialierClassMixin(GetDetailedSerializerClassMixin, GetRegularSerializerClassMixin):
	pass


class RegularModelInfoMixin(RegularSerialierMixin, FindModelMixin):
	pass


class DetailedModelInfoMixin(DetaliedSerialierClassMixin, FindModelMixin):
	pass
