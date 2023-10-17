from typing import Any, Dict
from projects.models import Project
from django_components import component

@component.register(name="project_tile")
class ProjectTile(component.Component):
    template_name="project_tile/project_tile.html"

    def get_context_data(self, project: Project, *args, **kwargs) -> Dict[str, Any]:
        return {
            "project": project
        }