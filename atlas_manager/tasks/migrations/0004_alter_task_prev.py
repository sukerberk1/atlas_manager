# Generated by Django 4.2.6 on 2023-10-24 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_remove_task_next_task_prev'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='prev',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='next', to='tasks.task'),
        ),
    ]