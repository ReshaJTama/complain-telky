import ipaddress, IPy
from django.shortcuts import render
from django.http import HttpResponse
from .models import complain_base,dir_base
from django.template import loader,Context
from django.template.loader import get_template,render_to_string
from  django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
import datetime,time

import sys, socket
from django.core.mail import send_mail
# Create your views here.

def index(request):
	list_table = complain_base.objects.all()
	context = {
		'title':'Complain Telky',
		'header':'Complain Telky',
		'list_table':list_table
	}
	return render(request,'list.html',context)

def list_toko(request):
	

	list_table = complain_base.objects.all()

	cek = complain_base.objects.get()

	context = {
		'title':'Complain Telky',
		'header':'Complain Telky',
		'list_table':list_table,
		'ip_address':ip_address,
		'status':x

# 		'id':list_table.id,
# 		'kode_toko':list_table.kode_toko,
# 		'sid':list_table.sid,
# 		'ip_address':list_table.ip_address,
# 		'ip_public':list_table.ip_public,

	}
	return render(request,'list.html',context)

@login_required
def email(request,id):
	authenticate()

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
	username = request.user.username
	msg_html = render_to_string('email.html',{'kode_toko':kode_toko,'ip_public':ip_public,'sid':sid,'username':username})
	date = datetime.date.today()
	times = time.time()


	log =dir_base(description=kode_toko,ip_public=ip_public,customer_id=sid,date_t=date,ip_addr=ip_address,time_t=times)
	log.save()
	try:

		send_mail(
			'Jaringan Bermasalah',
			'Mohon di bantu jaringan astinet bermasalah',
			'edp_net2@bgr2.indomaret.co.id',
			['edp_net@bgr2.indomaret.co.id'],
			fail_silently=False,
			html_message = msg_html,
			)

		return HttpResponse('Berhasil di Kirim')
	except:
		return HttpResponse('Gagal dikirim')

def logs(request):
	log = dir_base.objects.all()
	context = {
		'log':log
	}
	return render(request,'logs.html',context)
