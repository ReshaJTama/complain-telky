from django.urls import path
from . import views

urlpatterns = [
	path('',views.index, name='complain'),
	path('email/',views.email)
]