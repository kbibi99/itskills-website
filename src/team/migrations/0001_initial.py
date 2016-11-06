# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-18 21:58
from __future__ import unicode_literals

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
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree_name', models.CharField(blank=True, max_length=500, null=True)),
                ('institute_name', models.CharField(blank=True, max_length=500, null=True)),
                ('graduation_type', models.CharField(blank=True, max_length=500, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('date_of_graduation', models.CharField(blank=True, max_length=500, null=True)),
                ('period_of_studies', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_mail', models.CharField(blank=True, max_length=500, null=True)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Interests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InternShip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=500, null=True)),
                ('period', models.CharField(blank=True, max_length=500, null=True)),
                ('mission', models.CharField(blank=True, max_length=500, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=500, null=True)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=500, null=True)),
                ('last_name', models.CharField(blank=True, max_length=500, null=True)),
                ('slug', models.SlugField(unique=True)),
                ('owner_title', models.CharField(blank=True, max_length=500, null=True)),
                ('company_title', models.CharField(blank=True, max_length=500, null=True)),
                ('born_date', models.CharField(blank=True, max_length=500, null=True)),
                ('born_plase', models.CharField(blank=True, max_length=500, null=True)),
                ('adress', models.CharField(blank=True, max_length=500, null=True)),
                ('picture_index', models.FileField(upload_to=b'')),
                ('picture_cv', models.FileField(upload_to=b'')),
                ('cv_pdf', models.FileField(upload_to=b'')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(blank=True, max_length=500, null=True)),
                ('project_type', models.CharField(blank=True, max_length=500, null=True)),
                ('project_period', models.CharField(blank=True, max_length=500, null=True)),
                ('used_technologies', models.CharField(blank=True, max_length=500, null=True)),
                ('owner', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='team.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Recongnitions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('owner', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='team.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Skill_title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_title', models.CharField(blank=True, max_length=500, null=True)),
                ('owner', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='team.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(blank=True, max_length=500, null=True)),
                ('skill_percent', models.CharField(blank=True, max_length=500, null=True)),
                ('skill_title', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='team.Skill_title')),
            ],
        ),
        migrations.CreateModel(
            name='SocialExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comunity_name', models.CharField(blank=True, max_length=500, null=True)),
                ('owner_title', models.CharField(blank=True, max_length=500, null=True)),
                ('working_period', models.CharField(blank=True, max_length=500, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('owner', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='team.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='SotialNetAdress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sotial_network_adress', models.CharField(blank=True, max_length=500, null=True)),
                ('owner', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='team.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='TeamTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_title', models.CharField(blank=True, max_length=50, null=True)),
                ('team_description', models.CharField(blank=True, max_length=500, null=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=500, null=True)),
                ('work_period', models.CharField(blank=True, max_length=500, null=True)),
                ('mission', models.CharField(blank=True, max_length=500, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('owner', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='team.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='phonenumber',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='team.Profile'),
        ),
        migrations.AddField(
            model_name='internship',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='team.Profile'),
        ),
        migrations.AddField(
            model_name='interests',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='team.Profile'),
        ),
        migrations.AddField(
            model_name='email',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='team.Profile'),
        ),
        migrations.AddField(
            model_name='education',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='team.Profile'),
        ),
    ]