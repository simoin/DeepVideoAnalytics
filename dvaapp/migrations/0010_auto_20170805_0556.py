# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-05 05:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0009_auto_20170804_0651'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='parent_query',
            new_name='parent_process',
        ),
        migrations.RemoveField(
            model_name='tevent',
            name='clustering',
        ),
        migrations.RemoveField(
            model_name='tevent',
            name='event_type',
        ),
    ]
