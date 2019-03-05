from django.shortcuts import render
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

def email(request):
	send_mail(
			'Testing',
			'Ayam',
			'foolgum01@gmail.com',
			['kambing2933@gmail.com'],
			fail_silently=False,
		)
