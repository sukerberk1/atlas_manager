from typing import Any, Dict
from django_components import component
from django.contrib.auth.models import User

@component.register(name="user_avatar")
class UserAvatar(component.Component):
    template_name="user_avatar/user_avatar.html"

    def get_context_data(self, user: User, *args, **kwargs) -> Dict[str, Any]:
        context = {  } 
        if user.first_name and user.last_name:
            context["sign"] = user.first_name[0].capitalize() + user.last_name[0].capitalize()
        else:
            context["sign"] = user.username[0].capitalize()
        return context