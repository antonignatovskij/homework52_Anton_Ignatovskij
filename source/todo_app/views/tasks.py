from urllib.parse import urlencode

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


from todo_app.forms import TaskForm, SearchForm, ProjectForm, MembersForm
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


class ProjectDetailView(DetailView):
    template_name = 'tasks/project_detail.html'
    model = Project
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.object
        user = self.request.user
        context['is_captain'] = user.groups.filter(name='Капитан').exists()
        return context


class ProjectCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'tasks/project_create.html'
    form_class = ProjectForm
    permission_required = 'todo_app.add_project'

    def get_success_url(self):
        return reverse('tasks:project_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        self.object = form.save()
        self.object.members.add(self.request.user)
        return super().form_valid(form)


class ProjectUpdateView(PermissionRequiredMixin,UpdateView):
    model = Project
    template_name = 'tasks/project_update.html'
    form_class = ProjectForm
    context_object_name = 'project'
    permission_required = 'todo_app.change_project'

    def has_permission(self) -> bool:
        project = self.get_object()
        return (
                super().has_permission() and
                project.members.filter(pk=self.request.user.pk).exists()
        )


class ProjectDeleteView(PermissionRequiredMixin,DeleteView):
    template_name = 'tasks/project_detail.html'
    model = Project
    context_object_name = 'project'
    success_url = reverse_lazy('tasks:projects')
    permission_required = 'todo_app.delete_project'

    def has_permission(self) -> bool:
        project = self.get_object()
        return (
                super().has_permission() and
                project.members.filter(pk=self.request.user.pk).exists()
        )

class MembersUpdateView(PermissionRequiredMixin, UpdateView):
    model = Project
    form_class = MembersForm
    template_name = 'tasks/members_create.html'
    context_object_name = 'project'
    permission_required = 'todo_app.change_project'

    def get_success_url(self):
        return reverse('tasks:project_detail', kwargs={'pk': self.object.pk})

    def has_permission(self) -> bool:
        project = self.get_object()
        return (
                super().has_permission() and
                project.members.filter(pk=self.request.user.pk).exists()
                or
                project.members.filter(pk=self.request.user.pk).exists()
                and
                self.request.user.groups.filter(name='Капитан').exists()
        )



# ////вьюшки для тасков ниже


class TaskListView(ListView):
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        print(self.request.GET)
        return TodoItem.objects.all()



class TaskDetailView(DetailView):
    template_name = 'tasks/task_detail.html'
    model = TodoItem
    context_object_name = 'task'



class TaskCreateView(PermissionRequiredMixin,CreateView):
    model = TodoItem
    template_name = 'tasks/create_task.html'
    form_class = TaskForm
    permission_required = 'todo_app.change_todoitem'

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        task = form.save(commit=False)
        task.project = project
        task.save()
        task.type.set(form.cleaned_data['type'])
        return redirect('tasks:project_detail', pk=task.project.pk)

    def has_permission(self):
        project = get_object_or_404(Project, pk=self.kwargs["pk"])

        return (
                super().has_permission() and
                project.members.filter(pk=self.request.user.pk).exists()
        )


class TaskUpdateView(PermissionRequiredMixin,UpdateView):
    model = TodoItem
    template_name = 'tasks/update_task.html'
    form_class = TaskForm
    context_object_name = 'task'
    permission_required = 'todo_app.change_todoitem'


    def get_success_url(self):
        return reverse('tasks:project_detail', kwargs={'pk': self.object.project.pk})

    def has_permission(self):
        task = self.get_object()
        return (
                super().has_permission() and
                task.project.members.filter(pk=self.request.user.pk).exists()
        )


class TaskDeleteView(PermissionRequiredMixin,DeleteView):
    template_name = 'tasks/task_detail.html'
    model = TodoItem
    context_object_name = 'task'
    success_url = reverse_lazy('tasks:projects')
    permission_required = 'todo_app.change_todoitem'

    def has_permission(self):
        task = self.get_object()
        return (
                super().has_permission() and
                task.project.members.filter(pk=self.request.user.pk).exists()
        )

# add_logentry
# change_logentry
# delete_logentry
# view_logentry
# add_group
# change_group
# delete_group
# view_group
# add_permission
# change_permission
# delete_permission
# view_permission
# add_user
# change_user
# delete_user
# view_user
# add_contenttype
# change_contenttype
# delete_contenttype
# view_contenttype
# add_session
# change_session
# delete_session
# view_session
# add_project
# change_project
# delete_project
# view_project
# add_status
# change_status
# delete_status
# view_status
# add_todoitem
# change_todoitem
# delete_todoitem
# view_todoitem
# add_type
# change_type
# delete_type
# view_type
#
# add_logentry
# change_logentry
# delete_logentry
# view_logentry
# add_group
# change_group
# delete_group
# view_group
# add_permission
# change_permission
# delete_permission
# view_permission
# add_user
# change_user
# delete_user
# view_user
# add_contenttype
# change_contenttype
# delete_contenttype
# view_contenttype
# add_session
# change_session
# delete_session
# view_session
# add_project
# change_project
# delete_project
# view_project
# add_status
# change_status
# delete_status
# view_status
# add_todoitem
# change_todoitem
# delete_todoitem
# view_todoitem
# add_type
# change_type
# delete_type
# view_type

