# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-19 15:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hadoop_backup_catalog', '0013_auto_20180705_1701'),
    ]

    operations = [
        migrations.CreateModel(
            name='backup_recovery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=60)),
                ('cluster_name', models.CharField(max_length=60)),
                ('application_name', models.CharField(max_length=60)),
                ('list_of_files', models.CharField(max_length=60)),
                ('recovery_timestamp', models.DateTimeField(null=True)),
                ('requested_timestamp', models.DateTimeField(null=True)),
                ('status', models.CharField(max_length=25)),
                ('recovery_state', models.CharField(max_length=25)),
                ('recovery_job_id', models.IntegerField()),
                ('recovery_start_time', models.DateTimeField(null=True)),
                ('recovery_end_time', models.DateTimeField(null=True)),
                ('staging_directory', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'backup_recovery',
            },
        ),
        migrations.AlterField(
            model_name='backupoperations',
            name='completion_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='backupoperations',
            name='last_backup_timestamp',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='backupoperations',
            name='start_time',
            field=models.DateTimeField(null=True),
        ),
    ]
