# Generated by Django 3.1.6 on 2021-02-23 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voucher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voucher',
            name='quantity',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
    ]
