import ipaddress, IPy
from django.shortcuts import render
from django.http import HttpResponse
from .models import complain_base
from django.template import loader

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

	ip_public = items.ip_public

		#Kode Toko
	kode_toko = items.description

		#Customer_ID
	sid = items.customer_id
	if sid is not None:
		sid
	else:
		sid = 'No SID'
	# body = "<table>"ip_address+' '+kode_toko+' '+sid+"</table>"
	body = "<table border=1><tr><td>Kode Toko</td><td>"+kode_toko+"</td></tr><tr><td>IP Public</td><td>"+ip_public+"</td></tr><tr><td>SID</td><td>"+sid+"</td></tr><tr><td>PIC Toko</td><td>NO HP</td></tr></table>"
	print(id)
	try:
		send_mail(
			'Jaringan Bermasalah',
			body,
			'user01@test.com',
			['user02@test.com'],
			fail_silently=False,
			html_message = body,
			)
		return HttpResponse('Berhasil di Kirim')
	except:
		return HttpResponse('Gagal dikirim')