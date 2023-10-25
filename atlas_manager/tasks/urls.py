from django.urls import path
from .views import TasksTemplateView, TaskDetailView

urlpatterns = [
    path("template/", TasksTemplateView.as_view(), name="tasks"),
    path("<int:pk>", TaskDetailView.as_view(), name="task_detail")
]
