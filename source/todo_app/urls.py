from django.urls import path
from .views import tasklist, create_task, task_detail, update_task, delete_task

urlpatterns = [
    path('', tasklist, name='task_list'),
    path('add_task/', create_task, name='create'),
    path('task/<int:pk>/', task_detail, name='detail'),
    path('task/<int:pk>/update/', update_task, name='update'),
    path('task/<int:pk>/delete/', delete_task, name='delete'),
]
