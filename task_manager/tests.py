from django.contrib.auth import get_user_model
from django.template.context_processors import request
from django.test import TestCase, RequestFactory
from django.urls import reverse

from task_manager.models import Position, Worker, TaskType, Task
from task_manager.views import TaskListView, TaskCreatedListView


class ModelTest(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="Test Position")
        self.worker = get_user_model().objects.create_user(
            username="user",
            password="pass",
            first_name="Super",
            last_name="Man",
        )
        self.task_type = TaskType.objects.create(name="Test Task Type")
        self.task = Task.objects.create(
            name="Test Task",
            priority="Medium",
            task_type=self.task_type,
            author=self.worker,
        )
        self.task.assignees.set([self.worker])

    def test_string_representation(self):
        self.assertEqual(str(self.position), "Test Position")
        self.assertEqual(str(self.worker), "Super Man")
        self.assertEqual(str(self.task_type), "Test Task Type")
        self.assertEqual(str(self.task), "Test Task")

    def test_worker(self):
        self.assertEqual(self.worker.position, None)
        self.worker.position = self.position
        self.assertEqual(self.worker.position, self.position)

    def test_task(self):
        self.assertEqual(self.task.author, self.worker)
        self.assertEqual(self.task.task_type, self.task_type)
        self.assertEqual(list(self.task.assignees.all()), [self.worker])


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
            reverse("task_manager:position-list"),
            reverse("task_manager:position-create"),
            reverse("task_manager:position-update", kwargs={"pk": 1}),
            reverse("task_manager:position-delete", kwargs={"pk": 1}),
            reverse("task_manager:profile"),
            reverse("task_manager:profile-update", kwargs={"pk": 1}),
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
        url = reverse("task_manager:profile")
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

class TestViews(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.position = Position.objects.create(name="Test Position")
        self.worker = get_user_model().objects.create_user(
            username="user",
            password="pass",
            first_name="Super",
            last_name="Man",
        )
        self.worker2 = get_user_model().objects.create_user(
            username="user2",
            password="pass",
            first_name="Test",
            last_name="2",
        )
        self.task_type = TaskType.objects.create(name="Test Task Type")
        self.task = Task.objects.create(
            name="Test Task",
            priority="Medium",
            task_type=self.task_type,
            author=self.worker,
        )
        self.task2 = Task.objects.create(
            name="Test Task 2",
            priority="Low",
            task_type=self.task_type,
            author=self.worker2,
        )
        self.task.assignees.set([self.worker2])
        self.task2.assignees.set([self.worker])
        self.client.force_login(self.worker)

    def test_task_list(self):
        request = self.factory.get("task_manager:task-list")
        test = TaskListView(request=request)
        test.request.user = self.worker
        queryset = test.get_queryset()
        self.assertIn(self.task2, queryset)
        self.assertNotIn(self.task, queryset)

    def test_task_created(self):
        request = self.factory.get("task_manager:task-created")
        test = TaskCreatedListView(request=request)
        test.request.user = self.worker
        queryset = test.get_queryset()
        self.assertIn(self.task, queryset)
        self.assertNotIn(self.task2, queryset)
