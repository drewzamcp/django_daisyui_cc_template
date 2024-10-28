from django.contrib import admin
from main_project_fldr.core.models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ['description', 'is_completed', 'user']
admin.site.register(Todo, TodoAdmin)