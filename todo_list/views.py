from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView

from todo_list.models import Task, Tag


class TaskListView(ListView):
    model = Task
    template_name = "todo_list/index.html"
    paginate_by = 5

    def get_queryset(self):
        return Task.objects.all()


class TaskCreateView(generic.CreateView):
    model = Task
    fields = ["content", "deadline_datetime", "is_done", "tags"]
    success_url = reverse_lazy("todo_list:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = ["content", "deadline_datetime", "is_done", "tags"]
    success_url = reverse_lazy("todo_list:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo_list:index")


class TagListView(ListView):
    model = Tag
    paginate_by = 5
    template_name = "todo_list/tags.html"

    def get_queryset(self):
        return Tag.objects.all()


class TagsCreateView(generic.CreateView):
    model = Tag
    fields = ["name"]
    success_url = reverse_lazy("todo_list:tags")


class TagsUpdateView(generic.UpdateView):
    model = Tag
    fields = ["name"]
    success_url = reverse_lazy("todo_list:tags")


class TagsDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo_list:tags")


def toggle_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return JsonResponse({"status": "success"})
