# Generated by Django 3.2 on 2023-06-21 09:32

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20230621_0652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(datetime.datetime(2023, 6, 21, 9, 32, 24, 150777))]),
        ),
    ]
