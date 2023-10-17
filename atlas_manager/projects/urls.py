from django.urls import path
from .views import AllProjectsView

urlpatterns = [
    path("", AllProjectsView.as_view(), name="projects")
]
