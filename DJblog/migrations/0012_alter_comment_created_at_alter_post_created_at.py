# Generated by Django 5.0 on 2024-06-20 11:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DJblog', '0011_comment_comment_alter_comment_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 6, 20, 11, 46, 36, 28207, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 6, 20, 11, 46, 36, 28207, tzinfo=datetime.timezone.utc)),
        ),
    ]