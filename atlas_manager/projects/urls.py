from django.urls import path
from .views import ProjectsTemplateView, ProjectsListView

urlpatterns = [
    path("template/", ProjectsTemplateView.as_view(), name="projects"),
    path("", ProjectsListView.as_view(), name="get_projects"),
]
