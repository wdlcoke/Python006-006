# Generated by Django 2.2.13 on 2021-03-01 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstorder', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='owner',
        ),
    ]
