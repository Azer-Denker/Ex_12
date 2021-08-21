# Generated by Django 2.2.13 on 2021-08-21 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_advert_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advert',
            name='is_active',
        ),
        migrations.AddField(
            model_name='advert',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='advert',
            name='photo_img',
            field=models.ImageField(blank=True, null=True, upload_to='advert_pics', verbose_name='Картинка'),
        ),
    ]