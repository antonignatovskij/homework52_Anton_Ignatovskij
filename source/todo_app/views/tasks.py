from multiprocessing import context
from urllib.parse import urlencode

from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView, FormView, ListView

from todo_app.forms import TaskForm, SearchForm
from todo_app.models import TodoItem, Project


# Create your views here.

class ProjectListView(ListView):
    template_name = 'tasks/projects_list.html'
    model = Project
    context_object_name = 'projects'
    queryset = Project.objects.all()
    paginate_by = 5

    def dispatch(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SearchForm()
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(Q(project_title__icontains=self.search_value) | Q(project_description__icontains=self.search_value))
        return queryset



    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']


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


class TaskCreateView(FormView):
    template_name = 'tasks/create_task.html'
    form_class = TaskForm

    def form_valid(self, form):
        task = form.save()
        return redirect('detail', pk=task.pk)


class TaskUpdateView(View):
    def dispatch(self, request, *args, **kwargs):
        self.task = get_object_or_404(TodoItem, pk=self.kwargs.get('pk'))
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = TaskForm(instance=self.task)
        context = {'form': form}
        return render(request, 'tasks/update_task.html', context)

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST, instance=self.task)
        if form.is_valid():
            task = form.save()
            task.type.set(form.cleaned_data['type'])
            task.save()
            return redirect('detail', pk=task.pk)
        return render(request, 'tasks/update_task.html', {'form': form})


class TaskDeleteView(View):
    def post(self, request, *args, **kwargs):
        task = get_object_or_404(TodoItem, pk=kwargs.get('pk'))
        task.delete()
        return redirect('task_list')
