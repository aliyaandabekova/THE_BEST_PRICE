from django.contrib import admin
from .models import *



class ShopAdmin(admin.ModelAdmin):
    list_display = ['name','url','rate','amount_rate','count_rate','avg_rate']
    readonly_fields = ['rate','amount_rate','count_rate','avg_rate']

admin.site.register(Shop,ShopAdmin)
admin.site.register(Comment)

