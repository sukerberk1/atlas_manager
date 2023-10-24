from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from projects.models import Project

# Create your views here.

class TasksTemplateView(TemplateView):
    template_name = "tasks.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projects"] = Project.objects.filter(author=self.request.user)
        return context
    