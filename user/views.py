from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views import generic

from user.forms import WorkerCreationForm, WorkerUpdateForm
from user.models import Position, Worker


class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position


class PositionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    fields = ["name"]
    success_url = reverse_lazy("user:position-list")


class PositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    fields = ["name"]
    success_url = reverse_lazy("user:position-list")


class PositionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Position
    success_url = reverse_lazy("user:position-list")


class WorkerCreateView(generic.CreateView):
    model = Worker
    form_class = WorkerCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"


class Profile(LoginRequiredMixin, generic.View):
    template_name = "user/profile.html"

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, self.template_name)


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    form_class = WorkerUpdateForm
    success_url = reverse_lazy("user:profile")
