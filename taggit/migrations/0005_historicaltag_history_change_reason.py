# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-06 21:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0004_auto_20171123_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaltag',
            name='history_change_reason',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
