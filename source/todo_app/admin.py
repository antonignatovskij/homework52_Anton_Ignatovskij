from django.contrib import admin

from todo_app.models import TodoItem, Type, Status

# Register your models here.

admin.site.register(TodoItem)
admin.site.register(Type)
admin.site.register(Status)
