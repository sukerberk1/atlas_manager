# Generated by Django 4.2.6 on 2023-10-17 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_project_client_alter_project_group_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
