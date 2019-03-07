import ipaddress, IPy
from django.shortcuts import render
from django.http import HttpResponse
from .models import complain_base

from django.core.mail import send_mail
# Create your views here.

def index(request):
	list_table = complain_base.objects.all()
	context = {
		'title':'Complain Telky',
		'header':'Complain Telky',
		'list_table':list_table
	}
	return render(request,'index.html',context)

def email(request,id):
	
	context = {
		'items': complain_base.objects.get(id=id)
	}
	items = complain_base.objects.get(id=id)
		
		# IP Address
	test = items.ip_addr
	ip_address = IPy.IP(test).strNormal()

		#Kode Toko
	kode_toko = items.description

		#Customer_ID
	sid = items.customer_id
	if sid is not None:
		sid
	else:
		sid = 'No SID'
	return HttpResponse(ip_address+' '+kode_toko+' '+sid)
	# body = '<table><tr><td>Kode Toko </td><td>:</td><td></td></tr></table>'
	# print(id)
	# try :
	# 	send_mail(
	# 			'Testing',
	# 			'Ayam',
	# 			'foolgum01@gmail.com',
	# 			['kambing2933@gmail.com'],
	# 			fail_silently=False,
	# 		)
	# 	return HttpResponse(body)
	# except:
	# 	return HttpResponse('email tidak terkirim')