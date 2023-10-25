from typing import Any, Dict
from tasks.models import Task
from django_components import component

@component.register(name="task_chain")
class TaskChain(component.Component):
    template_name = "task_chain/task_chain.html"

    def get_context_data(self, task: Task, *args, **kwargs) -> Dict[str, Any]:
        return {
            "task": task
        }