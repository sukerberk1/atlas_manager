from typing import Any, Dict
from django_components import component

@component.register(name="nav_element")
class NavElement(component.Component):
    template_name="nav_element/nav_element.html"

    def get_context_data(self, *args, **kwargs) -> Dict[str, Any]:
        return {
            "title": kwargs.get("title", ""),
            "href": kwargs.get("href", ""),
        }
    
    class Media:
        css = "nav_element/nav_element.css"