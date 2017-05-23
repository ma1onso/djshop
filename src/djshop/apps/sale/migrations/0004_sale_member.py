# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-23 12:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0010_auto_20170523_1241'),
        ('sale', '0003_auto_20170510_0913'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='member',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sales', to='club.Member'),
        ),
    ]
