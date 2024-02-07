from django.contrib import admin

from .models import Constants


# Register your models here.

class AddConstant(admin.ModelAdmin):
    list_display = ('key', 'value','description')
    list_display_links = ('key','value')
    search_fields = ('key', 'value')



admin.site.register(Constants,AddConstant)



