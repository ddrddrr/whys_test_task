from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .mixins import RegularModelInfoMixin, DetailedModelInfoMixin, RegularSerialierMixin
from rest_framework import status


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


class ModelCreateView(RegularSerialierMixin, generics.CreateAPIView):
	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		response_data = serializer.data
		if 'id' in self.request.data[list(self.request.data.keys())[0]].keys():
			response_data['warning'] = 'do not provide id for creation, it is generated automatically'
		headers = self.get_success_headers(serializer.data)
		return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)
