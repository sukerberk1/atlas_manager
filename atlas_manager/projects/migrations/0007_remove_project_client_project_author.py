# Generated by Django 4.2.6 on 2023-10-24 17:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0006_alter_projectcolorgroup_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='client',
        ),
        migrations.AddField(
            model_name='project',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
