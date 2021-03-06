# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-03-06 21:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_auto_20180302_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='dlpsequencingdetail',
            name='rev_comp_override',
            field=models.CharField(blank=True, choices=[('i7,i5', 'No Reverse Complement'), ('i7,rev(i5)', 'Reverse Complement i5'), ('rev(i7),i5', 'Reverse Complement i7'), ('rev(i7),rev(i5)', 'Reverse Complement i7 and i5')], default=None, max_length=50, null=True, verbose_name='Reverse Complement Override'),
        ),
    ]
