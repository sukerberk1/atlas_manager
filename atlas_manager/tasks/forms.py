from django import forms
from .models import Task

class ProjectTaskCreateForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ("title",)
