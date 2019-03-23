from django.db import models

# Create your models here.

class complain_base(models.Model):
	ip_addr = models.IntegerField(null=False)
	description = models.CharField(max_length=64)
	customer_id = models.DecimalField(max_digits=50,decimal_places=3)
	ip_public = models.CharField(max_length=20)

	class Meta :
		managed = False
		db_table = 'ipaddresses'

	def __str__(self):
		return "{}.{}.{}".format(self.id,self.description,self.ip_addr)
	