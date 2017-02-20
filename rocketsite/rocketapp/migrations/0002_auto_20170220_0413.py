# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 04:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rocketapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flightlog',
            name='altitude',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='flightlog',
            name='delay',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='flightlog',
            name='flight_result',
            field=models.CharField(choices=[('SS', 'Success'), ('NF', 'No Fire'), ('LD', 'Late Deploy'), ('ND', 'No Deploy'), ('CA', 'CATO')], default='NF', max_length=2),
        ),
        migrations.AddField(
            model_name='flightlog',
            name='motor',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='rocket',
            name='max_altitude',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rocket',
            name='max_motor_diam',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rocket',
            name='weight',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='flightlog',
            name='launch_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='flightlog',
            name='notes_text',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='rocket',
            name='flight_count',
            field=models.IntegerField(default=0),
        ),
    ]