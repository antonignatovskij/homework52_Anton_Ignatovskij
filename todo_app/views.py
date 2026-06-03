from django.http import HttpResponseRedirect
from django.shortcuts import render

from todo_app.models import TodoItem
from todo_app.new_task_validator import NewTaskValidator


# Create your views here.

def tasklist(request):
    tasks = TodoItem.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

def create_task(request):
    if request.method == 'POST':
        new_task = {
            'description': request.POST.get('description').strip(),
            'status': request.POST.get('status').strip(),
            'date': request.POST.get('date').strip(),
        }
        if new_task['date'] == '':
            new_task['date'] = None
        print(new_task)
        flag = NewTaskValidator.validate_new_task(new_task)
        if flag == True:
            task = TodoItem.objects.create(
                description = new_task['description'],
                status = new_task['status'],
                date = new_task['date'],
            )
        else:
            varning = {'varning': flag}
            return render(request, 'create_task.html', varning)
        return HttpResponseRedirect('/')
    return render(request, 'create_task.html')