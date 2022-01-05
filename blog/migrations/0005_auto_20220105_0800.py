# Generated by Django 3.2.11 on 2022-01-05 08:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20220105_0755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2022, 1, 5, 8, 0, 0, 379845, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 5, 8, 0, 0, 379868, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='object_id',
            field=models.PositiveIntegerField(db_index=True),
        ),
    ]