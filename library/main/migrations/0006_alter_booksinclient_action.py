# Generated by Django 4.0.3 on 2022-04-01 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_booksinclient_date_of_taking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booksinclient',
            name='action',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.actions'),
        ),
    ]