# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-06 02:24
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0010_auto_20170805_0556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='region',
            name='metadata_json',
        ),
        migrations.RemoveField(
            model_name='tube',
            name='metadata_json',
        ),
        migrations.AddField(
            model_name='region',
            name='metadata',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tube',
            name='metadata',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]
