from django.contrib import admin

from .models import complain_base,dir_base
# Register your models here.

admin.site.register(complain_base)
admin.site.register(dir_base)