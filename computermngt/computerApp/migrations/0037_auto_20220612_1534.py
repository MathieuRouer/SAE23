# Generated by Django 2.2.25 on 2022-06-12 15:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0036_auto_20220612_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2022, 6, 12, 15, 34, 35, 2246)),
        ),
    ]
