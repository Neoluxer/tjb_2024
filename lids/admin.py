from django.contrib import admin

from .models import Lids


# Register your models here.

class AddLids_admin(admin.ModelAdmin):
    list_display = ('name','town','date_now')
    list_display_links = ('name',)
    search_fields = ('name','town')



admin.site.register(Lids,AddLids_admin)


