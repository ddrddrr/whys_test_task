from django.db import models
### I could not sit and look at the combination of czech and english variable names :)

# null=True is not needed for char/text fields
class AttributeName(models.Model):
	name = models.CharField(max_length=100, blank=True)
	code = models.CharField(max_length=100, blank=True)
	show = models.BooleanField(default=False, blank=True)


class AttributeValue(models.Model):
	value = models.CharField(max_length=100)


class Attribute(models.Model):
	attribute_name = models.ForeignKey(AttributeName, on_delete=models.CASCADE)
	attribute_value = models.ForeignKey(AttributeValue, on_delete=models.CASCADE)
