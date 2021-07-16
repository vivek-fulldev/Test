from django.db import models

# Create your models here.

class Products(models.Model):
	name = models.CharField('Name',max_length=50)
	weight = models.PositiveIntegerField('Weight (in Kg)')
	price = models.PositiveIntegerField('Price (in Ruppes)')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "Product"

	def __str__(self):
		return self.name