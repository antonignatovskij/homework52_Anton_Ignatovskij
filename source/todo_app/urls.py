from django.urls import path
from .views import tasklist, create_task

urlpatterns = [
    path('', tasklist),
    path('add_task/', create_task),
]
