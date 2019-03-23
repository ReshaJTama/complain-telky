from django.shortcuts import render
from django.http import HttpResponse
import os,socket,IPy

from .models import network_base

s = socket.socket()


# Create your views here.

# def index(request):
# 	netbase = network_base.objects.all()
# 	lim = network_base.objects.count()

# 	# for iploop in netbase:
# 	# 	iploop = iploop.id.all()
# 	# 	ip_address = IPy.IP(iploop.ip_addr).strNormal()
# 		# host = socket.gethostbyname(ip_address)		
# 		# port = 139
# 	# 	try:
# 	# 		s.recv(1024)
# 	# 		s.connect((host,port))
# 	# 		return HttpResponse(ip_address+' HOST IS UP')
# 	# 	except:
# 	# 		return HttpResponse(ip_address+' HOST IS DOWN')

# 	# ip_address = IPy.IP(ip_address).strNormal()
# 	# print(ip_address)

# 	for net in netbase:
# 		nets = net.ip_addr
# 		ids = net.id
# 		ip_address = IPy.IP(nets).strNormal()

# 		print(ip_address)
# 		context = {
# 			'id':ids,
# 			'ip_address':ip_address
# 		}
# 		return render(request,'net/index.html',context)

# 		# try:
# 		# 	host = socket.gethostbyname(ip_address)
# 		# 	port = 139
# 		# 	s.recv(1024)
# 		# 	s.connect((host,port))
# 		# 	return HttpResponse(ip_address+" HOST  IS UP")
# 		# except:
# 		# 	return HttpResponse(ip_address+" HOST  IS DOWN")

	

# 	# try:
# 	# 	host = socket.gethostbyname(ip_address)
# 	# 	port = 139
# 	# 	s.recv(1024)
# 	# 	s.connect((host,port))
# 	# 	return HttpResponse('HOST UP')
# 	# except:
# 	# 	return HttpResponse('HOST DOWN')


def ipaddr(request,id):
	list_table = network_base.objects.get(id=id)

	ip_address = IPy.IP(list_table.ip_addr).strNormal()
	host = socket.gethostbyname(ip_address)
	port = 139

	try:
		s.recv(1024)
		s.connect((host,port))
		context = {
			'cek':'HOST UP',
			'ip_address':ip_address
		}
		return render(request,'list.html',context)
	except:
		context = {
			'cek':'HOST DOWN',
			'ip_address':ip_address
		}
		return render(request,'list.html',context)


def index(request):
	list_table = network_base.objects.all()
	context = {
		'title':'Complain Telky',
		'header':'Complain Telky',
		'list_table':list_table
	}
	return render(request,'list.html',context)
	
	# context = {
	# 	'title':'Complain Telky',
	# 	'header':'Complain Telky',
	# 	'list_table':list_table,
	# }
	# return render(request,'list.html',context)
