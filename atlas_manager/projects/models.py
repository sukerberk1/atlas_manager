from django.db import models
from clients.models import Client

# Create your models here.

class ProjectGroupColor(models.Model):
    red = models.SmallIntegerField()
    green = models.SmallIntegerField()
    blue = models.SmallIntegerField()

class Project(models.Model):
    name = models.CharField(max_length=255)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="projects")
    group = models.ForeignKey(ProjectGroupColor, on_delete=models.SET_NULL, related_name="projects", null=True)