from django.test import TestCase

from django.contrib.auth import get_user_model
from django.urls import reverse


class TestAdminRequired(TestCase):
    def setUp(self):
        self.worker = get_user_model().objects.create_user(
            username="user",
            password="pass",
            first_name="Super",
            last_name="Man",
        )

    def test_without_login(self):
        urls = [
            reverse("task_manager:task-type-list"),
            reverse("task_manager:task-type-create"),
            reverse("task_manager:task-type-update", kwargs={"pk": 1}),
            reverse("task_manager:task-type-delete", kwargs={"pk": 1}),
            reverse("user:position-list"),
            reverse("user:position-create"),
            reverse("user:position-update", kwargs={"pk": 1}),
            reverse("user:position-delete", kwargs={"pk": 1}),
            reverse("user:profile"),
            reverse("user:profile-update", kwargs={"pk": 1}),
            reverse("task_manager:task-list"),
            reverse("task_manager:task-create"),
            reverse("task_manager:task-update", kwargs={"pk": 1}),
            reverse("task_manager:task-detail", kwargs={"pk": 1}),
            reverse("task_manager:task-delete", kwargs={"pk": 1}),
            reverse("task_manager:task-created"),
            reverse("task_manager:task-complete", kwargs={"pk": 1}),
        ]
        for url in urls:
            res = self.client.get(url)
            self.assertEqual(res.status_code, 302)

    def test_with_login(self):
        self.client.force_login(self.worker)
        url = reverse("user:profile")
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
