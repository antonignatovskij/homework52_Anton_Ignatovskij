from urllib.parse import urlencode

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from todo_app.forms import TaskForm, SearchForm, ProjectForm
from todo_app.models import TodoItem, Project





# Create your views here.

class ProjectListView(LoginRequiredMixin, ListView):
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


class ProjectDetailView(LoginRequiredMixin,DetailView):
    template_name = 'tasks/project_detail.html'
    model = Project


class ProjectCreateView(LoginRequiredMixin, CreateView):
    template_name = 'tasks/project_create.html'
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('tasks:project_detail', kwargs={'pk': self.object.pk})


class ProjectUpdateView(LoginRequiredMixin,UpdateView):
    model = Project
    template_name = 'tasks/project_update.html'
    form_class = ProjectForm
    context_object_name = 'project'


    def get_success_url(self):
        return reverse('tasks:project_detail', kwargs={'pk': self.object.pk})


class ProjectDeleteView(LoginRequiredMixin,DeleteView):
    template_name = 'tasks/project_detail.html'
    model = Project
    context_object_name = 'project'
    success_url = reverse_lazy('tasks:projects')



# ////вьюшки для тасков ниже


class TaskListView(LoginRequiredMixin,ListView):
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        print(self.request.GET)
        return TodoItem.objects.all()



class TaskDetailView(LoginRequiredMixin,DetailView):
    template_name = 'tasks/task_detail.html'
    model = TodoItem
    context_object_name = 'task'



class TaskCreateView(LoginRequiredMixin,CreateView):
    model = TodoItem
    template_name = 'tasks/create_task.html'
    form_class = TaskForm

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        task = form.save(commit=False)
        task.project = project
        task.save()
        task.type.set(form.cleaned_data['type'])
        return redirect('tasks:project_detail', pk=task.project.pk)


class TaskUpdateView(LoginRequiredMixin,UpdateView):
    model = TodoItem
    template_name = 'tasks/update_task.html'
    form_class = TaskForm
    context_object_name = 'task'


    def get_success_url(self):
        return reverse('tasks:project_detail', kwargs={'pk': self.object.project.pk})


class TaskDeleteView(LoginRequiredMixin,DeleteView):
    template_name = 'tasks/task_detail.html'
    model = TodoItem
    context_object_name = 'task'
    success_url = reverse_lazy('tasks:projects')



