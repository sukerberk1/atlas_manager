from django_components import component

@component.register(name="navbar")
class Navbar(component.Component):
    template_name = "navbar/navbar.html"