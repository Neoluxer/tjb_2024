from django.contrib import admin
from .models import Offer

# Register your models here.
class OfferAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'town',
                    'offer_number',
                    'published',
                    'value',
                    'id',
                    'area',
                    'addres',
                    'ruberic',
                    'customer',
                    'project_composition',)
    list_display_links = ('title','addres','value','customer')
    search_fields = ('title',
                    'town',
                    'offer_number',
                    'published',
                    'value',
                    'id',
                    'area',
                    'addres',
                    'ruberic',
                    'customer',
                    'project_composition',)

admin.site.register(Offer)