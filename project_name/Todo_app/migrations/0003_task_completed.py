# Generated by Django 5.0.3 on 2024-03-09 19:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Todo_app", "0002_remove_task_completed_remove_task_due_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="completed",
            field=models.BooleanField(default=False),
        ),
    ]
