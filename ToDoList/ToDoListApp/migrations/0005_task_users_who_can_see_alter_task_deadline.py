# Generated by Django 5.0.7 on 2024-08-29 17:25

import ToDoListApp.models.task
import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoListApp', '0004_task_state_alter_task_deadline_alter_task_owner_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='users_who_can_see',
            field=models.ManyToManyField(null=True, related_name='all_tasks', to=settings.AUTH_USER_MODEL, verbose_name='همه کاربرانی که تسک را می\u200cبینند'),
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateField(default=datetime.date(2024, 8, 29), max_length=10, validators=[ToDoListApp.models.task.validate_date], verbose_name='زمان سرسید'),
        ),
    ]