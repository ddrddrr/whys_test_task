from rest_framework import serializers
from rest_framework.reverse import reverse
from django.core.exceptions import ObjectDoesNotExist


class UrlIdSerializer(serializers.ModelSerializer):
	"""
		Adds id and URL field support.
		URL is the link to the page with information about specific model.
		ID is the user_defined_id instead of built-in one.
	"""

	class Meta:
		abstract = True

	id = serializers.IntegerField(read_only=False)
	url = serializers.SerializerMethodField(read_only=True, required=False)

	def get_url(self, obj):
		request = self.context.get('request', '')
		if request and request.method == 'GET':
			# Nested serializers can return Model.objects.none()
			try:
				model_name = obj.__class__.__name__
			except Exception as _:
				return None
			return reverse(
					'model-retrieve',
					kwargs={'model_name': model_name, 'pk': obj.pk},
					request=request
			)

	def save(self):
		provided_id = self.validated_data['id']
		model = self.Meta.model
		try:
			instance = model.objects.get(id=provided_id)
		except ObjectDoesNotExist as _:
			created = super().create(self.validated_data)
			return created

		return super().update(instance=instance, validated_data=self.validated_data)
