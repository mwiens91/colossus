# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-09-21 18:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20170915_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='librarysampledetail',
            name='lims_vial_barcode',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='LIMS vial barcode'),
        ),
    ]
