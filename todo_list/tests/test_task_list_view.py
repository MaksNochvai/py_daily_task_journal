from django.test import TestCase
from django.urls import reverse
from todo_list.models import Task


class TaskListViewTest(TestCase):
    def test_task_list_view(self):
        # Create some test tasks
        Task.objects.create(content="Task 1")
        Task.objects.create(content="Task 2")

        url = reverse("todo_list:index")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Task 1")
        self.assertContains(response, "Task 2")
