from django.db import models


class UserDefinedIdModel(models.Model):
	#id = models.IntegerField(unique=True)
	#_actual_id = models.AutoField(primary_key=True)

	class Meta:
		abstract = True
