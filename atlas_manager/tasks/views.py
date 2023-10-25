from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from projects.models import Project
from tasks.models import Task

# Create your views here.

class TasksTemplateView(TemplateView):
    template_name = "tasks.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_projects = Project.objects.filter(author=self.request.user)
        project_tasks = []
        for p in user_projects:
            tasks = p.tasks.filter(prev=None)
            project_tasks.append(tasks)
        context["project_tasks"] = project_tasks
        return context
