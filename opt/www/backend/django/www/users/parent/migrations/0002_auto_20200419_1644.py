# Generated by Django 3.0.5 on 2020-04-19 16:44

import django.contrib.sites.managers
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('parent', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='parent',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.AddField(
            model_name='parent',
            name='site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sites_parent', to='sites.Site'),
        ),
    ]
