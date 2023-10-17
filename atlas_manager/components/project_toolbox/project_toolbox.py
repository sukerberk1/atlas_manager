from django_components import component

@component.register(name="project_toolbox")
class ProjectToolbox(component.Component):
    template_name="project_toolbox/project_toolbox.html"