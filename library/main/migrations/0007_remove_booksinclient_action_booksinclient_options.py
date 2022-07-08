# Generated by Django 4.0.3 on 2022-04-01 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_booksinclient_action'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booksinclient',
            name='action',
        ),
        migrations.AddField(
            model_name='booksinclient',
            name='options',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.actions'),
        ),
    ]