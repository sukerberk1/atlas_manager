from typing import Any, Dict
from projects.models import ProjectColorGroup
from django_components import component

@component.register(name="project_group_tile")
class ProjectGroupTile(component.Component):
    template_name = "project_group_tile/project_group_tile.html"
    
    def get_context_data(self, group: ProjectColorGroup, *args, **kwargs) -> Dict[str, Any]:
        if "cancel" in kwargs:
            group = ProjectColorGroup()
        return {
            "group": group
        }