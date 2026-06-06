from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from todo_app.forms import TaskForm
from todo_app.models import TodoItem
from todo_app.new_task_validator import NewTaskValidator
from todo_app.validators import validate_task


# Create your views here.

def tasklist(request):
    tasks = TodoItem.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})

def create_task(request):
    form = TaskForm()
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {'form': form})
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = TodoItem(
                description = form.cleaned_data.get('description'),
                status = form.cleaned_data.get('status'),
                date = form.cleaned_data.get('date'),
                detail_description = form.cleaned_data.get('detail_description'),
            )
            new_task.save()
            return redirect('detail', pk=new_task.pk)
        else:
            return render(request, 'tasks/create_task.html', {'form': form})



def task_detail(request, pk, *args, **kwargs):
    task = get_object_or_404(TodoItem, pk=pk)
    context = {'task': task}
    return render(request, 'tasks/task_detail.html', context)


def update_task(request, pk, *args, **kwargs):
    todoitem = get_object_or_404(TodoItem, pk=pk)
    form = TaskForm(initial={'description': todoitem.description, 'status': todoitem.status, 'date': todoitem.date, 'detail_description': todoitem.detail_description})
    context = {'form': form}
    if request.method == 'GET':
        context['action'] = reverse("update", kwargs={'pk': todoitem.pk})
        return render(request, 'tasks/update_task.html', context)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            todoitem.description = request.POST.get('description')
            todoitem.status = request.POST.get('status')
            todoitem.date = request.POST.get('date')
            todoitem.detail_description = request.POST.get('detail_description')
            todoitem.save()
            return redirect('detail', pk=todoitem.pk)

        else:
            return render(request, 'tasks/update_task.html', {'form': form})

def delete_task(request, pk, *args, **kwargs):
    if request.method == 'POST':
        todoitem = get_object_or_404(TodoItem, pk=pk)
        todoitem.delete()
    return redirect('task_list')