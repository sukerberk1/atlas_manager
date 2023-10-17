from django.db import models
from clients.models import Client

# Create your models here.

#TODO: Add validator for rgb values
class ProjectColorGroup(models.Model):
    red = models.SmallIntegerField(default=255)
    green = models.SmallIntegerField(default=255)
    blue = models.SmallIntegerField(default=255)

class Project(models.Model):
    name = models.CharField(max_length=255)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="projects", null=True, blank=True)
    group = models.ForeignKey(ProjectColorGroup, on_delete=models.SET_NULL, related_name="project", null=True, blank=True)

    def get_color_hex(self):
        if self.group is None:
            return "#ffffff"
        return f"#{self.group.red, 'x'}"+f"{self.group.green, 'x'}"+f"{self.group.blue, 'x'}"
    
    def __str__(self) -> str:
        if self.client is None:
            return self.name + " [No client assigned]"
        return self.name + " " + self.client.first_name + " " + self.client.last_name