from django.urls import path
from .views import TasksTemplateView, TaskDetailView, TaskDeleteView, TaskCheckView

urlpatterns = [
    path("template/", TasksTemplateView.as_view(), name="tasks"),
    path("<int:pk>", TaskDetailView.as_view(), name="task_detail"),
    path("<int:pk>/delete", TaskDeleteView.as_view(), name="task_delete"),
    path("<int:pk>/check", TaskCheckView.as_view(), name="task_check"),
]
