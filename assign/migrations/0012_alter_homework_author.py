# Generated by Django 5.0.4 on 2024-04-17 00:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assign', '0011_alter_course_creator'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='author',
            field=models.ForeignKey(limit_choices_to={'profile__role': 'teacher'}, on_delete=django.db.models.deletion.CASCADE, related_name='assign_homeworks', to=settings.AUTH_USER_MODEL),
        ),
    ]
