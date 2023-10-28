from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView, DetailView, DeleteView, FormView
from .models import Project, ProjectColorGroup
from tasks.forms import ProjectTaskCreateForm

# Create your views here.

class ProjectsTemplateView(LoginRequiredMixin, TemplateView):
    template_name="projects.html"


class ProjectsListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "project_list.html"
    context_object_name = "projects"

    def post(self, request, *args, **kwargs) -> HttpResponse:
        prefix = self.request.POST.get('search', '')  # Get the parameter from the POST request

        # Filter products based on the 'category' parameter using istartswith
        if prefix:
            self.queryset = Project.objects.filter(name__istartswith=prefix)
        else:
            self.queryset = Project.objects.all()

        return self.get(request, *args, **kwargs)
    
    # If query parameter group exists, filter queryset by a group
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        query_group_name = self.request.GET.get("group", "")
        if query_group_name:
            g = ProjectColorGroup.objects.get(name=query_group_name)
            self.queryset = Project.objects.filter(group=g)
        return super().get(request, *args, **kwargs)


class ProjectGroupTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "groups.html"


class ProjectGroupListView(LoginRequiredMixin, ListView):
    model = ProjectColorGroup
    template_name = "group-list.html"
    context_object_name = "project_groups"


class ProjectDetailView(DetailView):
    model = Project
    template_name = "project-detail.html"
    context_object_name = "project"


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = "project_delete.html"
    success_url = reverse_lazy("projects")


class AddTaskView(FormView):
    form_class = ProjectTaskCreateForm
    template_name = "add_task.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["object"] = get_object_or_404(Project, pk=self.kwargs.get("pk"))
        return context
    
    def get_success_url(self) -> str:
        url = reverse_lazy("tasks")
        project_param = "?p=" + str(self.kwargs.get("pk"))
        return url + project_param

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get("pk"))

        task = form.save(commit=False)
        task.project = project
        task.save()

        return super().form_valid(form)
    
