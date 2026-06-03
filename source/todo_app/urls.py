from django.urls import path
from .views import tasklist, create_task, task_detail

urlpatterns = [
    path('', tasklist),
    path('add_task/', create_task),
    path('task/<int:pk>/', task_detail)
]
