# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-05 08:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hadoop_backup_catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='backupsets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appid', models.IntegerField()),
                ('boid', models.IntegerField()),
                ('bsid', models.IntegerField()),
                ('backupset_name', models.CharField(max_length=256)),
                ('status', models.CharField(max_length=24)),
                ('num_files', models.IntegerField()),
            ],
        ),
    ]
