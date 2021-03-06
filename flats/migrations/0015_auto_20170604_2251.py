# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-04 20:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('flats', '0014_auto_20170604_2200'),
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
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flats.City')),
            ],
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent_beginning', models.DateField(default=datetime.date.today, verbose_name='From')),
                ('rent_end', models.DateField(default=datetime.date.today, verbose_name='To')),
                ('flat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flats.Flat')),
            ],
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenant_nickname', models.CharField(max_length=40, unique=True)),
            ],
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
        migrations.AddField(
            model_name='availability',
            name='flat',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='flats.Flat'),
        ),
    ]
