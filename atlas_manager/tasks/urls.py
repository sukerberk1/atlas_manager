from django.urls import path
from .views import TasksTemplateView

urlpatterns = [
    path("template/", TasksTemplateView.as_view(), name="tasks"),
]
