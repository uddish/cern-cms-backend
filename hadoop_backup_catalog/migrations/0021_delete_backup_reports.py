# Generated by Django 2.0.7 on 2018-08-09 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hadoop_backup_catalog', '0020_backup_reports'),
    ]

    operations = [
        migrations.DeleteModel(
            name='backup_reports',
        ),
    ]
