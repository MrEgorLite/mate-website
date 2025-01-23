from django.urls import path

from user.views import (
    PositionCreateView,
    PositionUpdateView,
    PositionDeleteView,
    PositionListView,
    WorkerCreateView,
    Profile,
    WorkerUpdateView,
)

app_name = "user"

urlpatterns = [
    path("positions/", PositionListView.as_view(), name="position-list"),
    path(
        "positions/create/",
        PositionCreateView.as_view(),
        name="position-create",
    ),
    path(
        "positions/<int:pk>/update/",
        PositionUpdateView.as_view(),
        name="position-update",
    ),
    path(
        "positions/<int:pk>/delete/",
        PositionDeleteView.as_view(),
        name="position-delete",
    ),
    path("register/", WorkerCreateView.as_view(), name="register"),
    path("profile/", Profile.as_view(), name="profile"),
    path(
        "profile/<int:pk>/update/",
        WorkerUpdateView.as_view(),
        name="profile-update",
    ),
]
