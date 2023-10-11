from django.db import models
from clients.models import Client

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=255)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="projects")
    