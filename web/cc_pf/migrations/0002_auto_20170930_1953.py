# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 10:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cc_pf', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyset',
            name='apiSecret',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='keyset',
            name='apikey',
            field=models.CharField(max_length=50),
        ),
    ]
