from django.urls import path

from user.views import (
    PositionCreateView,
    PositionUpdateView,
    PositionDeleteView,
    PositionListView, WorkerCreateView, profile_view, WorkerUpdateView,
)

app_name = "user"

urlpatterns = [
    path("position/", PositionListView.as_view(), name="position-list"),
    path(
        "position/create/",
        PositionCreateView.as_view(),
        name="position-create",
    ),
    path(
        "position/<int:pk>/update/",
        PositionUpdateView.as_view(),
        name="position-update",
    ),
    path(
        "position/<int:pk>/delete/",
        PositionDeleteView.as_view(),
        name="position-delete",
    ),
    path("register/", WorkerCreateView.as_view(), name="register"),
    path("profile/", profile_view, name="profile"),
    path(
        "profile/<int:pk>/update/",
        WorkerUpdateView.as_view(),
        name="profile-update",
    ),
]