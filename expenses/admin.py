from django.contrib import admin

from .models import*


# Register your models here.

class AddExpenses_admin(admin.ModelAdmin):
    list_display = ('id', 'price', 'description', 'published')
    list_display_links = ('id', 'price', 'description', 'published')
    search_fields = ('id', 'price', 'description', 'published')


admin.site.register(AddExpenses, AddExpenses_admin)
