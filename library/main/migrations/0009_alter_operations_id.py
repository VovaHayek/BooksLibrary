# Generated by Django 4.0.3 on 2022-04-01 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_rename_booksinclient_operations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operations',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
