# Generated by Django 3.2.5 on 2022-01-02 16:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 2, 16, 55, 43, 484582, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 2, 16, 55, 43, 484618, tzinfo=utc)),
        ),
    ]
