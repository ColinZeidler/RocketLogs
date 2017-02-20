# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 06:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rocketapp', '0002_auto_20170220_0413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightlog',
            name='rocket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flights', to='rocketapp.Rocket'),
        ),
        migrations.AlterField(
            model_name='rocket',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rockets', to=settings.AUTH_USER_MODEL),
        ),
    ]
