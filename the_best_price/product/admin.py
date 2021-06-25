from django.contrib import admin
from .models import *



class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','date_created','shop','score_from_api','score_of_our_users']
    readonly_fields = ['date_created','score_from_api','score_of_our_users']
admin.site.register(Product,ProductAdmin)

admin.site.register(Score)