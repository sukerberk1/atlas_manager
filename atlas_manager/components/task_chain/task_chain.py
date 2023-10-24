from typing import Any, Dict
from django_components import component

@component.register(name="task_chain")
class TaskChain(component.Component):
    template_name = "task_chain/task_chain.html"

    def get_context_data(self, *args, **kwargs) -> Dict[str, Any]:
        return {
            "context" : 1
        }