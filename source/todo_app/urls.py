from django.urls import path
from .views import tasklist, create_task, task_detail

urlpatterns = [
    path('', tasklist, name='task_list'),
    path('add_task/', create_task, name='create'),
    path('task/<int:pk>/', task_detail, name='detail'),
]
