# Generated by Django 4.0.3 on 2022-04-22 12:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_operations_book_operations_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='operations',
            name='time_of_operation',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 22, 12, 31, 52, 14831, tzinfo=utc)),
        ),
    ]
