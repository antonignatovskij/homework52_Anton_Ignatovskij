from django.urls import path

from .views import (
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    ProjectListView,
    ProjectDetailView,
    ProjectCreateView
)

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('add_task/', TaskCreateView.as_view(), name='create'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='detail'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='delete'),
    path('projects/', ProjectListView.as_view(), name='projects'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('projects/add_project/', ProjectCreateView.as_view(), name='project_create'),
]
