from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic

from task_manager.forms import (
    WorkerCreationForm,
    WorkerUpdateForm
)
from task_manager.models import (
    Position,
    TaskType,
    Worker
)


class PositionListView(generic.ListView):
    model = Position


class PositionCreateView(generic.CreateView):
    model = Position
    fields = ["name"]
    success_url = reverse_lazy("task_manager:position-list")

class PositionUpdateView(generic.UpdateView):
    model = Position
    fields = ["name"]
    success_url = reverse_lazy("task_manager:position-list")

class PositionDeleteView(generic.DeleteView):
    model = Position
    success_url = reverse_lazy("task_manager:position-list")

class TaskTypeListView(generic.ListView):
    model = TaskType
    template_name = "task_manager/task_type_list.html"


class TaskTypeCreateView(generic.CreateView):
    model = TaskType
    template_name = "task_manager/task_type_form.html"
    fields = ["name"]
    success_url = reverse_lazy("task_manager:task-type-list")


class TaskTypeUpdateView(generic.UpdateView):
    model = TaskType
    template_name = "task_manager/task_type_form.html"
    fields = ["name"]
    success_url = reverse_lazy("task_manager:task-type-list")


class TaskTypeDeleteView(generic.DeleteView):
    model = TaskType
    template_name = "task_manager/task_type_confirm_delete.html"
    success_url = reverse_lazy("task_manager:task-type-list")


class WorkerCreateView(generic.CreateView):
    model = Worker
    form_class = WorkerCreationForm
    success_url = reverse_lazy("login")


def profile_view(request: HttpRequest) -> HttpResponse:
    return render(request, "task_manager/profile.html")


class WorkerUpdateView(generic.UpdateView):
    model = Worker
    form_class = WorkerUpdateForm
    success_url = reverse_lazy("task_manager:profile")
