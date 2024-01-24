from django.contrib import admin

from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display=('id', 'founder', 'project_name')
    list_display_link =('id', 'founder', 'project_name')
    list_filter = ('founder',)
    search_fields = ('founder', 'description', )
    list_per_page = 25

    
admin.site.register(Project, ProjectAdmin)



