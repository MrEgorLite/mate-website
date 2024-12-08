from django.urls import path

from task_manager.views import (
    TaskTypeListView,
    TaskTypeCreateView,
    TaskTypeUpdateView,
    TaskTypeDeleteView,
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskCreatedListView,
    TaskDetailView,
    complete_task,
)

app_name = "task_manager"

urlpatterns = [
    path("task-type/", TaskTypeListView.as_view(), name="task-type-list"),
    path(
        "task-type/create/",
        TaskTypeCreateView.as_view(),
        name="task-type-create",
    ),
    path(
        "task-type/<int:pk>/update/",
        TaskTypeUpdateView.as_view(),
        name="task-type-update",
    ),
    path(
        "task-type/<int:pk>/delete/",
        TaskTypeDeleteView.as_view(),
        name="task-type-delete",
    ),
    path("", TaskListView.as_view(), name="task-list"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path(
        "task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"
    ),
    path("task/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path(
        "task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"
    ),
    path("task/created/", TaskCreatedListView.as_view(), name="task-created"),
    path("task/<int:pk>/complete/", complete_task, name="task-complete"),
]
