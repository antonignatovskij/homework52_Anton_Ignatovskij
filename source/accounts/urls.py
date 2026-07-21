from django.urls import path

from todo_app.views import (
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    ProjectListView,
    ProjectDetailView,
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDeleteView
)

app_name = 'accounts'

urlpatterns = [
    # path('tasks/', TaskListView.as_view(), name='task_list'),

]
