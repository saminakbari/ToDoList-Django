# Generated by Django 4.2.11 on 2024-08-11 12:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ToDoListApp', '0006_alter_task_priority'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoList2',
            fields=[
                ('list_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('owner', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='to_do_lists', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]