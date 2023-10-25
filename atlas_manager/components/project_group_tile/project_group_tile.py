from typing import Any, Dict
from projects.models import ProjectColorGroup
from django_components import component

""" 
PROJECT GROUP TILE COMPONENT
Returns a square with light gradient of the given color group
params:
cancel - if given, generates white colorGroup which targets no group at all
hover - is hover functionality enabled
size - size of the generated square
"""
@component.register(name="project_group_tile")
class ProjectGroupTile(component.Component):
    template_name = "project_group_tile/project_group_tile.html"
    
    def get_context_data(self, group: ProjectColorGroup, *args, **kwargs) -> Dict[str, Any]:
        if "cancel" in kwargs:
            group = ProjectColorGroup()
        context = {}
        context["group"] = group
        if "hover" in kwargs:
            context["hover"] = True
        if "size" in kwargs:
            context["size"] = kwargs["size"]
        return context