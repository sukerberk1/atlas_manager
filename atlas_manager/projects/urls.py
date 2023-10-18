from django.urls import path
from .views import ProjectsTemplateView, ProjectsListView, ProjectGroupTemplateView, ProjectGroupListView

urlpatterns = [
    path("template/", ProjectsTemplateView.as_view(), name="projects"),
    path("", ProjectsListView.as_view(), name="get_projects"),
    path("groups/template", ProjectGroupTemplateView.as_view(), name="project_groups"),
    path("groups/", ProjectGroupListView.as_view(), name="get_project_groups"),
]
