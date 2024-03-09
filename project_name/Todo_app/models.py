from django.db import models

# Create your models here.
# models.py

from django.db import models

class Task(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    def __str__(self):
        return self.description
