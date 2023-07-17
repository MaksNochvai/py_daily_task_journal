from django.db import models


class Task(models.Model):
    content = models.TextField(max_length=155, blank=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    deadline_datetime = models.DateTimeField(blank=True, null=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag")

    class Meta:
        ordering = ['-is_done', '-created_datetime']

    def __str__(self):
        return self.content


class Tag(models.Model):
    name = models.CharField(max_length=55)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
