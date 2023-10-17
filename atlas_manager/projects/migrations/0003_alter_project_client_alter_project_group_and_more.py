# Generated by Django 4.2.6 on 2023-10-17 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
        ('projects', '0002_projectcolorgroup_project_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='clients.client'),
        ),
        migrations.AlterField(
            model_name='project',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project', to='projects.projectcolorgroup'),
        ),
        migrations.AlterField(
            model_name='projectcolorgroup',
            name='blue',
            field=models.SmallIntegerField(default=255),
        ),
        migrations.AlterField(
            model_name='projectcolorgroup',
            name='green',
            field=models.SmallIntegerField(default=255),
        ),
        migrations.AlterField(
            model_name='projectcolorgroup',
            name='red',
            field=models.SmallIntegerField(default=255),
        ),
    ]
