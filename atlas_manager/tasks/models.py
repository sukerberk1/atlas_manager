from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
from projects.models import Project

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks")
    prev = models.OneToOneField("self",null=True, blank=True, on_delete=models.DO_NOTHING, related_name="next")
    done = models.BooleanField(default=False)
    due = models.DateField(null=True, blank=True)

    def clean(self):
        super().clean()
        if self.prev:
            if self.prev.project != self.project:
                raise ValidationError("The previous task must belong to the same project.")
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def get_author(self):
        return self.project.author

    def __str__(self):
        return self.get_author().username + "'s task in project " + self.project.name + ": " + self.title
    

