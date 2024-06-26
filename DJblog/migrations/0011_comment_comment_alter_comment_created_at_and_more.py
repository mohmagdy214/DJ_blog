# Generated by Django 5.0 on 2024-06-20 11:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DJblog', '0010_alter_comment_created_at_alter_post_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 6, 20, 11, 44, 40, 169951, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 6, 20, 11, 44, 40, 169951, tzinfo=datetime.timezone.utc)),
        ),
    ]
