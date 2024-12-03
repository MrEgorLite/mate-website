from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from task_manager.models import Worker, Task


class WorkerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "position"
        )


class WorkerUpdateForm(UserChangeForm):
    class Meta:
        model = Worker
        fields = ["first_name", "last_name", "position"]


class TaskForm(forms.ModelForm):
    assignees = forms.ModelMultipleChoiceField(
        queryset=Worker.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Task
        fields = [
            "name",
            "description",
            "deadline",
            "priority",
            "task_type",
            "assignees",
        ]
