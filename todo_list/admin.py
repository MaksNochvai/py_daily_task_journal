from django.contrib import admin

from todo_list.models import Task, Tag

admin.register(Task)
admin.register(Tag)
