# Generated by Django 3.1.6 on 2021-02-23 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0014_auto_20210223_0615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addressinformation',
            name='is_same',
        ),
    ]