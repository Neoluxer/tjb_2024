from django.contrib import admin

from .models import*


# Register your models here.

class AddProfit_admin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'price', 'description', 'published')
    list_display_links = ('customer', 'price')
    search_fields = ('id', 'price', 'description', 'published')


admin.site.register(AddProfits,AddProfit_admin)
admin.site.register(Customer_category)
