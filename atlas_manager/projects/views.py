from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Project

# Create your views here.

class ProjectsTemplateView(TemplateView):
    template_name="projects.html"


class ProjectsListView(ListView):
    model = Project
    template_name = "project_list.html"
    context_object_name = "projects"

    def post(self, request, *args, **kwargs):
        prefix = self.request.POST.get('search', '')  # Get the parameter from the POST request

        # Filter products based on the 'category' parameter using istartswith
        if prefix:
            self.queryset = Project.objects.filter(name__istartswith=prefix)
        else:
            self.queryset = Project.objects.all()

        return self.get(request, *args, **kwargs)

