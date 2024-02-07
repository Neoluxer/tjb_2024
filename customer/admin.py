from django.contrib import admin

from .models import Customers,Private_person


# Register your models here.

class AddCustomer_admin(admin.ModelAdmin):
    list_display = ('fn', 'name', 'ln', 'phone','email','ct','published')
    list_display_links = ('fn', 'ln', 'name')
    search_fields = ('fn', 'ln', 'name')


admin.site.register(Customers, AddCustomer_admin)
admin.site.register(Private_person)
