# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-04 16:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flats', '0004_auto_20170531_2313'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flat',
            old_name='flat_id',
            new_name='address',
        ),
    ]