from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .utils import custom_400, get_model_name
from .mixins import RegularModelInfoMixin, DetailedModelInfoMixin, get_serializer_class


def api_home(request):
	return render(request, template_name="templates/home_page.html")


class ModelRetrieveView(RegularModelInfoMixin, generics.RetrieveAPIView):
	pass


class DetailedModelRetrieveView(DetailedModelInfoMixin, generics.RetrieveAPIView):
	pass


class ModelListView(RegularModelInfoMixin, generics.ListAPIView):
	pass


class DetailedModelListView(DetailedModelInfoMixin, generics.ListAPIView):
	pass


@api_view(['POST'])
def create_view(request):
	if not request.data:
		return custom_400('Data for model creation were not provided')

	data = request.data
	if isinstance(data, dict):  # if only one model provided
		data = [data]

	created_objects = dict()
	for model_data in data:
		try:
			model_name = get_model_name(model_data)
		except Exception as e:
			return custom_400(f"Wrong data format, could not retrieve model name\n{e}")

		attrs = model_data[model_name]

		sz_class = get_serializer_class(model_name)
		if not sz_class:
			return custom_400(f'Serializer for {model_name} does not exist')

		sz = sz_class(data=attrs)
		sz.is_valid()
		if sz.errors:
			return custom_400(sz.errors)
		try:
			sz.save()
		except KeyError as e:
			return custom_400(f'Id was not provided for {model_name}\n{e}')
		except Exception as e:
			return custom_400(f'Serializer could not create/update {model_name} instance with provided data\n{e}')

		if sz.validated_data.get('url', ''):
			created_objects[model_name] = sz.validated_data['url']
		else:
			created_objects[model_name] = sz.validated_data['id']

	return Response(
			data={'status': 'created', 'created_objects': created_objects},
			status=status.HTTP_201_CREATED
	)
