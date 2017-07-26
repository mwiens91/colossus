# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-07-31 17:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_remove_chipregionmetadata_metadata_field_old'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sublibraryinformation',
            name='chip_region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.ChipRegion', verbose_name='Chip_Region'),
        ),
    ]
