# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-23 12:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0006_creditcardreference_virtual_pos'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='autocheckout_secret_code_checksum',
            field=models.CharField(blank=True, default='', max_length=32, verbose_name='Checksum used for autocheckout'),
        ),
    ]
