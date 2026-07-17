from django.contrib import admin

from todo_app.models import TodoItem, Type, Status, Project

# Register your models here.

admin.site.register(TodoItem)
admin.site.register(Type)
admin.site.register(Status)
admin.site.register(Project)
