from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#TODO: Add validator for rgb values
class ProjectColorGroup(models.Model):
    name = models.CharField(max_length=127, unique=True)
    red = models.SmallIntegerField(default=255)
    green = models.SmallIntegerField(default=255)
    blue = models.SmallIntegerField(default=255)

    def get_color_hex(self):
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

    def __str__(self) -> str:
        return self.name + " " + self.get_color_hex()


class Project(models.Model):
    name = models.CharField(max_length=255)
    group = models.ForeignKey(ProjectColorGroup, on_delete=models.SET_NULL, related_name="project", null=True, blank=True)
    done = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_color_hex(self):
        if self.group is None:
            return "#ffffff"
        return self.group.get_color_hex()
    
    def __str__(self) -> str:
        return self.name + "; Author: " + self.author.username