# Generated by Django 5.0 on 2024-06-20 11:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DJblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 6, 20, 11, 15, 57, 178750, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 6, 20, 11, 15, 57, 178750, tzinfo=datetime.timezone.utc)),
        ),
    ]
