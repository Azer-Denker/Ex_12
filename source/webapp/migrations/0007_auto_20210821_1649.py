# Generated by Django 2.2.13 on 2021-08-21 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20210821_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='status',
            field=models.CharField(choices=[('new', 'Не модерировано'), ('moderated', 'Модерировано'), ('rejected', 'Отклонено')], default='new', max_length=15, null=True, verbose_name='Статус'),
        ),
    ]