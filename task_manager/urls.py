from django.urls import path

from task_manager.views import PositionCreateView, PositionListView, PositionUpdateView, PositionDeleteView

app_name = "task_manager"

urlpatterns = [
    path("position/", PositionListView.as_view(), name="position-list"),
    path("position/create/", PositionCreateView.as_view(), name="position-create"),
    path("position/<int:pk>/update/", PositionUpdateView.as_view(), name="position-update"),
    path("position/<int:pk>/delete/", PositionDeleteView.as_view(), name="position-delete"),
]
