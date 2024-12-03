from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseRedirect
)
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


class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position


class PositionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    fields = ["name"]
    success_url = reverse_lazy("task_manager:position-list")


class PositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    fields = ["name"]
    success_url = reverse_lazy("task_manager:position-list")


class PositionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Position
    success_url = reverse_lazy("task_manager:position-list")


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    template_name = "task_manager/task_type_list.html"


class TaskTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    template_name = "task_manager/task_type_form.html"
    fields = ["name"]
    success_url = reverse_lazy("task_manager:task-type-list")


class TaskTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TaskType
    template_name = "task_manager/task_type_form.html"
    fields = ["name"]
    success_url = reverse_lazy("task_manager:task-type-list")


class TaskTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TaskType
    template_name = "task_manager/task_type_confirm_delete.html"
    success_url = reverse_lazy("task_manager:task-type-list")


class WorkerCreateView(generic.CreateView):
    model = Worker
    form_class = WorkerCreationForm
    success_url = reverse_lazy("login")


@login_required
def profile_view(request: HttpRequest) -> HttpResponse:
    return render(request, "task_manager/profile.html")


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    form_class = WorkerUpdateForm
    success_url = reverse_lazy("task_manager:profile")


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task

    def get_queryset(self):
        queryset = Task.objects.filter(assignees__id=self.request.user.id)
        return queryset


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_manager:task-list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_manager:task-list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task_manager:task-list")


class TaskCreatedListView(LoginRequiredMixin, generic.ListView):
    model = Task

    def get_queryset(self):
        queryset = Task.objects.filter(author_id=self.request.user.id)
        return queryset


@login_required
def complete_task(request: HttpRequest, pk: int) -> HttpResponse:
    task = Task.objects.get(pk=pk)
    task.is_completed = not task.is_completed
    task.save()
    referer = request.META.get("HTTP_REFERER")
    if referer:
        return HttpResponseRedirect(referer)
    return HttpResponseRedirect(
        reverse("task_manager:task-detail", kwargs={"pk": pk}),
    )
