# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-23 12:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0007_member_autocheckout_secret_code_checksum'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=254, verbose_name='Email of the member'),
        ),
        migrations.AddField(
            model_name='member',
            name='telephone_number',
            field=models.CharField(blank=True, default='', max_length=32, verbose_name='Last name of the member'),
        ),
    ]
