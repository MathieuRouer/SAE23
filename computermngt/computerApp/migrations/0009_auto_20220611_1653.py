# Generated by Django 2.2.25 on 2022-06-11 16:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0008_auto_20220611_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2022, 6, 11, 16, 53, 37, 454212)),
        ),
    ]
