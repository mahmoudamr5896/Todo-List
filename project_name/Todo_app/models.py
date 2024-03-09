from django.db import models

# Create your models here.
# models.py

class Group(models.Model):
    name = models.CharField(max_length=100 )

    def __str__(self):
        return self.name

class TaskList(models.Model):
    name = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.PROTECT,blank=True, null=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.description