from django.db import models

# Create your models here.

class complain_base(models.Model):
	ip_address = models.CharField(max_length=15)
	kode_toko = models.CharField(max_length=4)
	nama_toko = models.CharField(max_length=50)
	sid = models.DecimalField(max_digits=25,decimal_places=3)
	ip_public = models.CharField(max_length=15)

	def __str__(self):
		return "{}.{}.{}".format(self.id,self.kode_toko,self.nama_toko)
	