from django.contrib import admin
from .models import *



class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','date_created','shop']
    readonly_fields = ['date_created']
admin.site.register(Product,ProductAdmin)