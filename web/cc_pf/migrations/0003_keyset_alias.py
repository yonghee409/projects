# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 10:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cc_pf', '0002_auto_20170930_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='keyset',
            name='alias',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
