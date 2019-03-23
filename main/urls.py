from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='complain'),
    path('',include('django.contrib.auth.urls')),
    path('complain/',include('complain.urls')),
    path('network/', include('network.urls')),
]
