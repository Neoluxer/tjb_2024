from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'area', 'address', 'published','ruberic')
    list_display_links = ('name',)
    search_fields = ('name', 'area', 'address', 'published',)


admin.site.register(Project,ProjectAdmin)
