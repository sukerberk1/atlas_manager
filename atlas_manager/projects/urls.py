from django.urls import path
from .views import *

urlpatterns = [
    path("template/", ProjectsTemplateView.as_view(), name="projects"),
    path("", ProjectsListView.as_view(), name="get_projects"),
    path("groups/template", ProjectGroupTemplateView.as_view(), name="project_groups"),
    path("groups/", ProjectGroupListView.as_view(), name="get_project_groups"),
    path("<int:pk>", ProjectDetailView.as_view(), name="project_detail"),
    path("<int:pk>/delete", ProjectDeleteView.as_view(), name="project_delete"),
    path("<int:pk>/create-task", AddTaskView.as_view(), name="project_add_task"),
]
