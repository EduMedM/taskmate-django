# Generated by Django 4.2 on 2023-09-04 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0002_task_done'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Task',
            new_name='TaskList',
        ),
    ]