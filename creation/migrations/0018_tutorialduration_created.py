# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-07-08 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creation', '0017_auto_20200702_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorialduration',
            name='created',
            field=models.DateTimeField(null=True),
        ),
    ]
