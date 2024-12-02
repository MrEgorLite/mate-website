from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic

from task_manager.forms import (
    WorkerCreationForm,
    WorkerUpdateForm, TaskForm
)
from task_manager.models import (
    Position,
    TaskType,
    Worker, Task
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


class TaskListView(generic.ListView):
    model = Task
    def get_queryset(self):
        queryset = Task.objects.filter(assignees__id=self.request.user.id)
        return queryset


class TaskDetailView(generic.DetailView):
    model = Task

class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_manager:task-list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_manager:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task_manager:task-list")


class TaskCreatedListView(generic.ListView):
    model = Task
    def get_queryset(self):
        queryset = Task.objects.filter(author_id=self.request.user.id)
        return queryset

def complete_task(request: HttpRequest, pk: int) -> HttpResponse:
    task = Task.objects.get(pk=pk)
    task.is_completed = not task.is_completed
    task.save()
    return HttpResponseRedirect(
        reverse("task_manager:task-detail", kwargs={"pk": pk}),
    )
