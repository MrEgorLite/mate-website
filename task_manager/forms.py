from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from task_manager.models import Worker


class WorkerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "position")


class WorkerUpdateForm(UserChangeForm):
    class Meta:
        model = Worker
        fields = ["first_name", "last_name", "position"]
