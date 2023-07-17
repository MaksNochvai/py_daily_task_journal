from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView

from todo_list.models import Task, Tag


class TaskListView(ListView):
    model = Task
    template_name = "base.html"
    paginate_by = 5


class TagListView(ListView):
    model = Tag
    paginate_by = 5
    template_name = "todo_list/tags.html"


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
