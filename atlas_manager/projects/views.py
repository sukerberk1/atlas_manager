from django.shortcuts import render
from django.views.generic import ListView
from .models import Project

# Create your views here.

class AllProjectsView(ListView):
    template_name="projects.html"
    model=Project
