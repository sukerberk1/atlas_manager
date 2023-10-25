from typing import Any
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from projects.models import Project
from tasks.models import Task

# Create your views here.

class TasksTemplateView(LoginRequiredMixin, TemplateView):
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

class TaskDetailView(UserPassesTestMixin, DetailView):
    model = Task
    template_name = "task_detail.html"
    context_object_name = "task"

    def test_func(self):
        task = self.get_object()
        return task.project.author == self.request.user
    

class TaskDeleteView(UserPassesTestMixin, DeleteView):
    model = Task
    template_name = "task_delete.html"
    success_url = reverse_lazy("tasks")

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        self.object = self.get_object()

        if self.object.prev:
            prev_task = self.object.prev
            next_task = self.object.next
            self.object.delete()

            next_task.prev = prev_task
            next_task.save()
        else:
            self.object.delete()
        
        return HttpResponseRedirect(self.get_success_url())
    
    def test_func(self):
        task = self.get_object()
        return task.project.author == self.request.user


class TaskCheckView(UpdateView):
    model = Task
    template_name = "task_check.html"
    success_url = reverse_lazy("tasks")
    fields=[]

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        self.object = self.get_object()
        self.object.done = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
