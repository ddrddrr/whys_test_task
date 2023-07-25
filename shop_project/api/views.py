from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .mixins import RegularModelInfoMixin, DetailedModelInfoMixin, get_serializer_class


def custom_400(msg):
	return Response({'status': 'error', 'error': msg}, status=status.HTTP_400_BAD_REQUEST)


def get_model_name(data):
	try:
		name = list(data.keys())[0]
	except Exception as ex:
		raise ex
	return name


def api_home(request):
	return render(request, template_name="templates/home_page.html", context={})


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
		except Exception as _:
			return custom_400("Wrong data format, could not retrieve model name")

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
		except Exception as ex:
			return custom_400(f'Serializer could not save {model_name} instance instantiated with provided data\n{ex}')

		url = sz.validated_data.get('url', '')
		if url:
			created_objects[model_name] = sz.validated_data['url']
		else:
			created_objects[model_name] = sz.validated_data['id']

	return Response(
			data={'status': 'created', 'created_objects': created_objects},
			status=status.HTTP_201_CREATED
	)

# class ModelCreateView(RegularSerialierMixin, generics.CreateAPIView):
# 	def create(self, request, *args, **kwargs):
# 		serializer = self.get_serializer(data=request.data)
# 		serializer.is_valid(raise_exception=True)
# 		self.perform_create(serializer)
# 		response_data = serializer.data
# 		if 'id' in self.request.data[list(self.request.data.keys())[0]].keys():
# 			response_data['warning'] = 'do not provide id for creation, it is generated automatically'
# 		headers = self.get_success_headers(serializer.data)
# 		return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)
