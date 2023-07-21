from django.test import TestCase, Client
from django.urls import reverse
from django.http import JsonResponse
from todo_list.models import Task, Tag


class ToggleTaskStatusViewTest(TestCase):
    def test_toggle_task_status_view(self):
        task = Task.objects.create(content="Toggle Task", is_done=False)
        url = reverse("todo_list:task-toggle-status", args=[task.pk])

        response = self.client.post(url)

        self.assertEqual(response.status_code, 200)
        task.refresh_from_db()
        self.assertTrue(task.is_done)

        # Test toggling again
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        task.refresh_from_db()
        self.assertFalse(task.is_done)
