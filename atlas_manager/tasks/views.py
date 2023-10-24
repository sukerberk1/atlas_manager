from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from projects.models import Project
from tasks.models import Task

# Create your views here.

class TasksTemplateView(TemplateView):
    template_name = "tasks.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = Task.objects.filter(project__author=self.request.user).filter(prev=None)
        return context
