# Generated by Django 5.0.7 on 2024-08-26 12:49

import ToDoListApp.models.task
import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoListApp', '0003_alter_task_deadline_alter_task_description'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='state',
            field=models.BooleanField(choices=[(False, 'Not Done'), (True, 'Done')], default=False, verbose_name='وضعیت'),
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateField(default=datetime.date(2024, 8, 26), max_length=10, validators=[ToDoListApp.models.task.validate_date], verbose_name='زمان سرسید'),
        ),
        migrations.AlterField(
            model_name='task',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasks', to=settings.AUTH_USER_MODEL, verbose_name='صاحب تسک'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='to_do_lists', to=settings.AUTH_USER_MODEL, verbose_name='صاحب لیست'),
        ),
    ]