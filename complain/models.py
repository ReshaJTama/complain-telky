from django.db import models
from django.utils import timezone
from datetime import timedelta

def timers():
	return timezone.localtime(timezone.now()) + timedelta(days=settings.DAYS)
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

class dir_base(models.Model):
	ip_addr = models.CharField(null=False,max_length=15)
	description = models.CharField(max_length=64)
	customer_id = models.CharField(max_length=50)
	ip_public = models.CharField(max_length=20,null=True)
	date_t = models.DateField(auto_now_add=True)
	time_t = models.TimeField(auto_now_add=True)

	def __str__(self):
		return "{}.{}.{}.{}".format(self.id,self.description,self.time_t,self.date_t)