# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-05 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hadoop_backup_catalog', '0009_auto_20180705_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backupoperations',
            name='appid',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='backupoperations',
            name='boid',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='backupoperations',
            name='elapsed_seconds',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='backupoperations',
            name='num_archives',
            field=models.IntegerField(null=True),
        ),
    ]
