from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from task_manager.models import Position


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
