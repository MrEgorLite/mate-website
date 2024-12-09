from django.test import TestCase

from django.contrib.auth import get_user_model

from task_manager.models import TaskType, Task
from user.models import Position


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
