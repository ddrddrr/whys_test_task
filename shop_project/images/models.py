from django.db import models


class Image(models.Model):
	source_url = models.URLField(default='')
	name = models.CharField(max_length=100, blank=True)
