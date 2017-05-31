# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 20:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flats', '0002_auto_20170531_2038'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent_beginning', models.DateField(default=datetime.date.today, verbose_name='From')),
                ('rent_end', models.DateField(default=datetime.date.today, verbose_name='To')),
            ],
        ),
        migrations.AddField(
            model_name='flat',
            name='rent_beginning',
            field=models.DateField(default=datetime.date.today, verbose_name='From'),
        ),
        migrations.AddField(
            model_name='flat',
            name='rent_end',
            field=models.DateField(default=datetime.date.today, verbose_name='To'),
        ),
        migrations.AlterField(
            model_name='city',
            name='city_name',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='flat',
            name='flat_id',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='tenant_nickname',
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.AddField(
            model_name='rent',
            name='flat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flats.Flat'),
        ),
        migrations.AddField(
            model_name='rent',
            name='tenant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flats.Tenant'),
        ),
        migrations.AddField(
            model_name='flat',
            name='rents',
            field=models.ManyToManyField(through='flats.Rent', to='flats.Tenant'),
        ),
    ]
