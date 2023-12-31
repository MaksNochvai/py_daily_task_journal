"""
URL configuration for Py_Todo_List project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from todo_list import views
from todo_list.views import (
    TaskListView,
    TagListView,
    TagsCreateView,
    TagsUpdateView,
    TagsDeleteView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView
)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path(
        "tasks/create/",
        TaskCreateView.as_view(),
        name="task-create",
    ),
    path(
        "tasks/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update",
    ),
    path(
        "tasks/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete",
    ),
    path("tags/", TagListView.as_view(), name="tags"),
    path(
        "tags/create/",
        TagsCreateView.as_view(),
        name="tags-create",
    ),
    path(
        "tags/<int:pk>/update/",
        TagsUpdateView.as_view(),
        name="tags-update",
    ),
    path(
        "tags/<int:pk>/delete/",
        TagsDeleteView.as_view(),
        name="tags-delete",
    ),
    path("tasks/<int:pk>/toggle-status/",
         views.toggle_task_status,
         name="task-toggle-status"),
]

app_name = "todo_list"
