from django.contrib import admin
from .models import Invoice


class InvoiceBase_admin(admin.ModelAdmin):
    list_display = ('id','name', 'sum', 'invoice_number', 'ruberic', 'customer','organisation')
    list_display_links = ('invoice_number',)
    search_fields = ('id','name', 'sum', 'invoice_number', 'ruberic', 'customer','organisation')


admin.site.register(Invoice,InvoiceBase_admin)
