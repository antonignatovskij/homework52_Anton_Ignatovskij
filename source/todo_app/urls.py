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

app_name = 'tasks'

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('projects/<int:pk>/add_task/', TaskCreateView.as_view(), name='create'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='detail'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='delete'),
    path('', ProjectListView.as_view(), name='projects'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('projects/add_project/', ProjectCreateView.as_view(), name='project_create'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('projects/<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
]
