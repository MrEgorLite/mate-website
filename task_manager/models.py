from datetime import datetime, tzinfo

import pytz
from django.db import models
from user.models import Worker


class TaskType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Task(models.Model):
    PRIORITY_CHOICES = (
        ("Critical", "Critical"),
        ("High", "High"),
        ("Medium", "Medium"),
        ("Low", "Low"),
    )
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(choices=PRIORITY_CHOICES, max_length=8)
    task_type = models.ForeignKey(
        TaskType, on_delete=models.SET_NULL, related_name="tasks", null=True
    )
    assignees = models.ManyToManyField(Worker, related_name="assigned_tasks")
    author = models.ForeignKey(
        Worker, on_delete=models.CASCADE, related_name="created_tasks"
    )

    @property
    def is_expired(self):
        return datetime.now(pytz.timezone("Europe/Kiev")) > self.deadline

    def __str__(self):
        return self.name
