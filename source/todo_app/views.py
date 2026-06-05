from multiprocessing import context

from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from todo_app.models import TodoItem
from todo_app.new_task_validator import NewTaskValidator
from todo_app.validators import validate_task


# Create your views here.

def tasklist(request):
    tasks = TodoItem.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})

def create_task(request):
    if request.method == 'GET':
        create_task_url = reverse("create")
        return render(request, 'tasks/create_task.html', context={'action': create_task_url})
    if request.method == 'POST':
        new_task = TodoItem(
            description = request.POST.get('description'),
            status = request.POST.get('status'),
            date = request.POST.get('date'),
            detail_description = request.POST.get('detail_description'),
        )
        errors = validate_task(new_task)
        if errors:
            context = {'errors': errors, 'task': new_task}
            return render(request, 'tasks/create_task.html', context)
        else:
            new_task.save()
            return redirect('detail', pk=new_task.pk)



def task_detail(request, pk, *args, **kwargs):
    task = get_object_or_404(TodoItem, pk=pk)
    context = {'task': task}
    return render(request, 'tasks/task_detail.html', context)


def update_task(request, pk, *args, **kwargs):
    todoitem = get_object_or_404(TodoItem, pk=pk)
    context = {'task': todoitem}
    if request.method == 'GET':
        context['action'] = reverse("update", kwargs={'pk': todoitem.pk})
        return render(request, 'tasks/update_task.html', context)
    if request.method == 'POST':
        todoitem.description = request.POST.get('description')
        todoitem.status = request.POST.get('status')
        todoitem.date = request.POST.get('date')
        todoitem.detail_description = request.POST.get('detail_description')
        errors = validate_task(todoitem)
        if errors:
            context['errors'] = errors
            return render(request, 'tasks/update_task.html', context)
        else:
            todoitem.save()
            return redirect('detail', pk=todoitem.pk)
    # if request.method == 'POST':
    #     new_task = {
    #         'description': request.POST.get('description').strip(),
    #         'status': request.POST.get('status').strip(),
    #         'date': request.POST.get('date').strip(),
    #         'detail_description': request.POST.get('detail_description'),
    #     }
    #     if new_task['date'] == '':
    #         new_task['date'] = None
    #     print(new_task)
    #     flag = NewTaskValidator.validate_new_task(new_task)
    #     if flag == True:
    #         todoitem.description = new_task['description']
    #         todoitem.status = new_task['status']
    #         todoitem.date = new_task['date']
    #         todoitem.detail_description = new_task['detail_description']
    #         todoitem.save()
    #     else:
    #         varning = {'varning': flag}
    #         return render(request, 'tasks/create_task.html', varning)
    #     return redirect('detail', pk=todoitem.pk)
    # return render(request, 'tasks/update_task.html', {'task': todoitem})

