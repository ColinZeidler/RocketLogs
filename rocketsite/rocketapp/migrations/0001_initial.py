# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 22:53
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FlightLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('launch_date', models.DateField(default=datetime.date.today)),
                ('notes_text', models.TextField(default='')),
                ('motor', models.CharField(default='', max_length=100)),
                ('delay', models.PositiveSmallIntegerField(default=0)),
                ('altitude', models.PositiveIntegerField(default=0)),
                ('flight_result', models.CharField(choices=[('SS', 'Success'), ('NF', 'No Fire'), ('LD', 'Late Deploy'), ('ND', 'No Deploy'), ('CA', 'CATO')], default='NF', max_length=2)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flights', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rocket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('flight_count', models.IntegerField(default=0)),
                ('weight', models.FloatField(default=0)),
                ('max_motor_diam', models.IntegerField(default=0)),
                ('max_altitude', models.IntegerField(default=0)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rockets', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='flightlog',
            name='rocket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flights', to='rocketapp.Rocket'),
        ),
    ]
