# Generated by Django 3.0.5 on 2020-05-03 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tokenteacher',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='auth_token_teacher', to='teacher.Teacher', verbose_name='Teacher'),
        ),
    ]
