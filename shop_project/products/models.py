from django.db import models
from attributes.models import Attribute
from images.models import Image


class Product(models.Model):
	CURRENCIES = [
		('CZK', 'Czech Crown'),
		('EUR', 'Euro'),
		('USD', 'US Dollar'),
		('GBP', 'British Pound'),
	]
	name = models.CharField(max_length=200, blank=True)
	description = models.CharField(max_length=2000, blank=True)
	price = models.DecimalField(default=0, max_digits=12, decimal_places=2)
	currency = models.CharField(max_length=3, choices=CURRENCIES, blank=True)
	published_on = models.DateTimeField(null=True, blank=True)
	is_published = models.BooleanField(default=False, blank=True)


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
	image = models.ForeignKey(Image, on_delete=models.CASCADE)
	name = models.CharField(max_length=100, blank=True)


class Catalog(models.Model):
	name = models.CharField(max_length=200, blank=True)
	image = models.ForeignKey(
			Image,
			null=True,
			blank=True,
			on_delete=models.SET_NULL
	)
	products = models.ManyToManyField(Product, blank=True)
	attributes = models.ManyToManyField(Attribute, blank=True)
