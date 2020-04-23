# Generated by Django 3.0.5 on 2020-04-23 06:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
        ('parent', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parent',
            name='student',
        ),
        migrations.CreateModel(
            name='ParentStudentMM',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parent_mm_student', to=settings.AUTH_USER_MODEL, verbose_name='parent_mm_student')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_mm_parent', to='student.Student', verbose_name='student_mm_parent')),
            ],
        ),
        migrations.AddField(
            model_name='parent',
            name='student',
            field=models.ManyToManyField(blank=True, null=True, related_name='student', through='parent.ParentStudentMM', to='student.Student', verbose_name='parent_student'),
        ),
    ]