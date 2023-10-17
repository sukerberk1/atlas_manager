from django.db import models
from clients.models import Client

# Create your models here.

#TODO: Add validator for rgb values
class ProjectColorGroup(models.Model):
    red = models.SmallIntegerField(default=255)
    green = models.SmallIntegerField(default=255)
    blue = models.SmallIntegerField(default=255)

    def __str__(self) -> str:
        r = f"{self.red:x}"
        g = f"{self.green:x}"
        b = f"{self.blue:x}"
        if len(r) == 1:
            r = "0" + r
        if len(g) == 1:
            g = "0" + g
        if len(b) == 1:
            b = "0" + b
        return "#"+r+g+b

class Project(models.Model):
    name = models.CharField(max_length=255)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="projects", null=True, blank=True)
    group = models.ForeignKey(ProjectColorGroup, on_delete=models.SET_NULL, related_name="project", null=True, blank=True)
    done = models.BooleanField(default=False)

    def get_color_hex(self):
        if self.group is None:
            return "#ffffff"
        return str(self.group)
    
    def __str__(self) -> str:
        if self.client is None:
            return self.name + " [No client assigned]"
        return self.name + " " + self.client.first_name + " " + self.client.last_name