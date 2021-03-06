# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-23 17:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Moviesdouban',
            fields=[
                ('field_id', models.AutoField(db_column='_id', primary_key=True, serialize=False)),
                ('directors', models.CharField(blank=True, max_length=1000, null=True)),
                ('rate', models.CharField(blank=True, max_length=500, null=True)),
                ('cover_x', models.IntegerField(blank=True, null=True)),
                ('star', models.CharField(blank=True, max_length=50, null=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('url', models.CharField(blank=True, max_length=250, null=True)),
                ('casts', models.CharField(blank=True, max_length=250, null=True)),
                ('cover', models.CharField(blank=True, max_length=250, null=True)),
                ('id', models.CharField(blank=True, max_length=100, null=True)),
                ('cover_y', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
