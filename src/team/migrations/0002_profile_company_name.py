# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 21:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='company_name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
