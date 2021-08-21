# Generated by Django 2.2.13 on 2021-08-21 07:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20210821_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Цена'),
        ),
    ]
