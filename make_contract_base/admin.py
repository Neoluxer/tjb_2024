from django.contrib import admin
from .models import ContractBase,Organization,PrivateContract
# Register your models here.

class ContractBase_admin(admin.ModelAdmin):
    list_display = ('number','date','customer_firm','total_cost','contract_file',)
    list_display_links = ('number',)
    search_fields = ('number','date','customer_firm')


admin.site.register(ContractBase,ContractBase_admin)
admin.site.register(Organization)
admin.site.register(PrivateContract)