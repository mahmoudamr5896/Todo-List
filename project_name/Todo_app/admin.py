from django.contrib import admin

# Register your models here.
from .models import Group, Task, TaskList

admin.site.register(Task)
admin.site.register(TaskList)
admin.site.register(Group)