from django.contrib.auth import get_user_model
from django.test import TestCase, RequestFactory

from task_manager.models import TaskType, Task
from task_manager.views import TaskListView, TaskCreatedListView
from user.models import Position


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
