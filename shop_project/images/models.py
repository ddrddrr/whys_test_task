from django.db import models


class Image(models.Model):
	obrazek = models.URLField('Odkaz na obrazek')
	nazev = models.CharField('Nazev', max_length=100, blank=True)
