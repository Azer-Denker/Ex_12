# Generated by Django 2.2.13 on 2021-08-21 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advert',
            name='price',
        ),
        migrations.AlterField(
            model_name='advert',
            name='status',
            field=models.CharField(choices=[('new', 'Не модерировано'), ('moderated', 'Модерировано'), ('rejected', 'Отклонено')], default='new', max_length=15, verbose_name='Статус'),
        ),
    ]
