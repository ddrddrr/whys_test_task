from django.db import models
from attributes.models import Attribute
from images.models import Image


# null=True is not needed for char/text fields and it leads to two definitions of "non-existent" string
class Product(models.Model):
	CURRENCIES = [
		('CZK', 'Czech Crown'),
		('EUR', 'Euro'),
		('USD', 'US Dollar'),
		('GBP', 'British Pound'),
	]
	nazev = models.CharField('Nazev', max_length=200, blank=True)
	description = models.CharField('Popis', max_length=2000, blank=True)
	cena = models.DecimalField('Cena', max_digits=12, decimal_places=2)
	mena = models.CharField('Mena', max_length=3, choices=CURRENCIES, blank=True)
	published_on = models.DateTimeField('Publikovano dne', null=True, blank=True)
	is_published = models.BooleanField('Publikovano', default=False, blank=True)


class ProductAttributes(models.Model):
	attribute = models.ForeignKey(
			Attribute,
			on_delete=models.CASCADE,
	)
	product = models.ForeignKey(
			Product,
			on_delete=models.CASCADE,
			related_name='attributes'
	)


class ProductImage(models.Model):
	product = models.ForeignKey(
			Product,
			on_delete=models.CASCADE,
			related_name='image'
	)
	obrazek = models.ForeignKey(Image, on_delete=models.CASCADE)
	nazev = models.CharField('Nazev', max_length=100, blank=True)


class Catalog(models.Model):
	nazev = models.CharField('Nazev', max_length=200, blank=True)
	obrazek = models.ForeignKey(
			Image,
			null=True,
			blank=True,
			on_delete=models.SET_NULL
	)
	products_ids = models.ManyToManyField(Product, blank=True)
	attributes_ids = models.ManyToManyField(Attribute, blank=True)
