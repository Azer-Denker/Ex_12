# Generated by Django 2.2.13 on 2021-08-21 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_auto_20210821_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='moderate',
            field=models.BooleanField(default=False),
        ),
    ]