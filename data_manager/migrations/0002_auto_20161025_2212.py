# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 05:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='data',
            name='description',
            field=models.TextField(default='none', max_length=2000),
        ),
        migrations.AddField(
            model_name='data',
            name='origin_path',
            field=models.FilePathField(default='none'),
        ),
        migrations.AddField(
            model_name='data',
            name='path_to_file',
            field=models.FilePathField(default='none'),
        ),
        migrations.AddField(
            model_name='data',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
