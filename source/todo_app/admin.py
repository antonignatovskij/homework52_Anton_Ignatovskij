from django.contrib import admin

from todo_app.models import TodoItem

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'status', 'date']
    list_filter = ['date']
    search_fields = ['description', 'status', 'date']
    fields = ['description', 'status', 'date']

admin.site.register(TodoItem, TodoAdmin)
