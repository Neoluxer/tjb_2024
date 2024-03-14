from django.contrib import admin
from .models import Builders
# Register your models here.

class Builders_admin(admin.ModelAdmin):
    list_display = ('id','ct', 'fn', 'name', 'ln', 'phone', 'price','portfolio_image')
    list_display_links = ('name',)
    search_fields = ('id','ct', 'fn', 'name', 'ln', 'phone',
                     'price','portfolio_image','segment','email')
admin.site.register(Builders,Builders_admin)