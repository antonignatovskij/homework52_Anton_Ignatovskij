from multiprocessing import context

from django.shortcuts import render, get_object_or_404, redirect

from django.views import View
from django.views.generic import TemplateView

from todo_app.forms import TaskForm
from todo_app.models import TodoItem

# Create your views here.

class TaskListView(TemplateView):
    template_name = 'tasks/index.html'

    def get_context_data(pk, *args, **kwargs):
        kwargs['tasks'] = TodoItem.objects.all()
        return super().get_context_data(**kwargs)


class TaskDetailView(TemplateView):
    template_name = 'tasks/task_detail.html'

    def get_context_data(self, **kwargs):
        kwargs['task'] = get_object_or_404(TodoItem, pk=kwargs.get('pk'))
        return super().get_context_data(**kwargs)

class TaskCreateView(View):
    def get(self, request, *args, **kwargs):
        form = TaskForm()
        return render(request, 'tasks/create_task.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect('detail', pk=task.pk)
        return render(request, 'tasks/create_task.html', {'form': form})


class TaskUpdateView(View):
    def dispatch(self, request, *args, **kwargs):
        self.task = get_object_or_404(TodoItem, pk=kwargs.get('pk'))
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = TaskForm(instance=self.task)
        context = {'form': form}
        return render(request, 'tasks/update_task.html', context)

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST, instance=self.task)
        if form.is_valid():
            task = form.save()
            return redirect('detail', pk=task.pk)
        return render(request, 'tasks/update_task.html', {'form': form})


class TaskDeleteView(View):
    def post(self, request, *args, **kwargs):
        task = get_object_or_404(TodoItem, pk=kwargs.get('pk'))
        task.delete()
        return redirect('task_list')
