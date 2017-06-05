# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-04 18:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flats', '0007_flat_free'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(default=datetime.date.today)),
                ('availability', models.BooleanField(default=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='flat',
            name='free',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='rent_beginning',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='rent_end',
        ),
        migrations.AddField(
            model_name='flat',
            name='availability',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='flats.Availability'),
        ),
    ]
