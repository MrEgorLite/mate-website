from django.urls import path

from task_manager.views import PositionCreateView, PositionListView, PositionUpdateView, PositionDeleteView, \
    TaskTypeListView, TaskTypeCreateView, TaskTypeUpdateView, TaskTypeDeleteView

app_name = "task_manager"

urlpatterns = [
    path("task-type/", TaskTypeListView.as_view(), name="task-type-list"),
    path("task-type/create/", TaskTypeCreateView.as_view(), name="task-type-create"),
    path("task-type/<int:pk>/update/", TaskTypeUpdateView.as_view(), name="task-type-update"),
    path("task-type/<int:pk>/delete/", TaskTypeDeleteView.as_view(), name="task-type-delete"),
    path("position/", PositionListView.as_view(), name="position-list"),
    path("position/create/", PositionCreateView.as_view(), name="position-create"),
    path("position/<int:pk>/update/", PositionUpdateView.as_view(), name="position-update"),
    path("position/<int:pk>/delete/", PositionDeleteView.as_view(), name="position-delete"),
]
