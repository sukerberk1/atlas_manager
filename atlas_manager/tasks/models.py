from django.db import models
from django.contrib.auth.models import User
from projects.models import Project

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    next = models.ForeignKey("self",null=True, blank=True, on_delete=models.DO_NOTHING, related_name="prev")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
    due = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.author.username + "'s task: " +self.title
    

