# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-05 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hadoop_backup_catalog', '0010_auto_20180705_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backuparchives_raw',
            name='handle_raw',
            field=models.TextField(),
        ),
    ]