# Generated by Django 2.0.7 on 2018-08-07 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hadoop_backup_catalog', '0016_auto_20180807_0741'),
    ]

    operations = [
        migrations.AddField(
            model_name='applications',
            name='username',
            field=models.CharField(default='null', max_length=30),
            preserve_default=False,
        ),
    ]