# Generated by Django 5.0 on 2024-06-20 11:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DJblog', '0005_alter_post_created_at_delete_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='drafted',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 6, 20, 11, 28, 16, 538990, tzinfo=datetime.timezone.utc)),
        ),
    ]
