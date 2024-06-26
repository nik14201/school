# Generated by Django 3.0.5 on 2020-05-17 12:21

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teacher', '0002_auto_20200517_1221'),
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('_name', models.CharField(blank=True, max_length=512, null=True, verbose_name='Name')),
                ('_code', models.CharField(blank=True, max_length=256, null=True, verbose_name='Code')),
                ('_school', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='school.MainModel', verbose_name='Школа')),
                ('_teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='teacher.User', verbose_name='Учитель')),
            ],
            options={
                'verbose_name': 'Предмет',
                'verbose_name_plural': 'Предмет',
                'db_table': 'subject',
            },
        ),
    ]
