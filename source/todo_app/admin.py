from django.contrib import admin

from todo_app.models import TodoItem, Type, Status

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'status', 'type', 'date_of_add', 'date_of_update']
    list_filter = ['date_of_add']
    search_fields = ['title', 'description', 'status', 'type', 'date_of_add', 'date_of_update']
    fields = ['title', 'description', 'status', 'type']
    readonly_fields = ['date_of_add', 'date_of_update']

admin.site.register(TodoItem, TodoAdmin)
admin.site.register(Type)
admin.site.register(Status)
