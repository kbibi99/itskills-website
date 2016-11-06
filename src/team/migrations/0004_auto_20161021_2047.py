# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_profile_owner_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='internship',
            old_name='description',
            new_name='description01',
        ),
        migrations.AddField(
            model_name='internship',
            name='description02',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]