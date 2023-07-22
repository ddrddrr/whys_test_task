from django.db import models


class AttributeName(models.Model):
	nazev = models.CharField("Nazev", max_length=100, blank=True)
	kod = models.CharField("Kod", max_length=100, blank=True)
	zobrazit = models.BooleanField("Zobrazit", default=False, blank=True)


class AttributeValue(models.Model):
	hodnota = models.CharField("Hodnota", max_length=100)


class Attribute(models.Model):
	nazev_atributu = models.ForeignKey(AttributeName, on_delete=models.CASCADE)
	hodnota_atributu = models.ForeignKey(AttributeValue, on_delete=models.CASCADE)
