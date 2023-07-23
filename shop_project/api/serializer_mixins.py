from rest_framework import serializers
from rest_framework.reverse import reverse


class SerializerUrlMixin(metaclass=serializers.SerializerMetaclass):
	"""Adds URL pointing to detailed view of a model"""
	url = serializers.SerializerMethodField(read_only=True, required=False)

	def get_url(self, obj):
		request = self.context.get('request', '')
		if request and request.method == 'GET':
			# Nested serializers can return Model.objects.none()
			try:
				model_name = obj.__class__.__name__
			except Exception as _:
				return ''
			return reverse(
					'model-retrieve',
					kwargs={'model_name': model_name, 'pk': obj.pk},
					request=request
			)
